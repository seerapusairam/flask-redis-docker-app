import time
import redis
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# Retry connecting to Redis on startup
r = None
for i in range(10):
    try:
        r = redis.Redis(host='redis', port=6379)
        r.ping()  # test connection
        print("Connected to Redis")
        break
    except redis.exceptions.ConnectionError:
        print(f"Redis connection failed, retrying {i+1}/10...")
        time.sleep(1)
else:
    raise Exception("Could not connect to Redis after 10 attempts")

@app.route('/hits')
def get_hits():
    try:
        count = r.get('hits')
        count = int(count) if count else 0
    except Exception as e:
        app.logger.error(f"Error fetching hits from Redis: {e}")
        count = 0
    return jsonify(hits=count)

@app.route('/')
def hello():
    try:
        r.incr('hits')
        count = r.get('hits')
        count = int(count) if count else 0
    except Exception as e:
        app.logger.error(f"Error incrementing hits in Redis: {e}")
        count = 0

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hit Counter</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .container { max-width: 400px; margin: auto; text-align: center; }
            h1 { color: #333; }
            #count { font-size: 3em; margin: 20px 0; }
            button {
                padding: 10px 20px;
                font-size: 1em;
                cursor: pointer;
                border: none;
                background-color: #007BFF;
                color: white;
                border-radius: 5px;
            }
            button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Visitor Hit Counter</h1>
            <div id="count">{{ count }}</div>
            <button onclick="refreshHits()">Refresh Count</button>
        </div>

        <script>
            function refreshHits() {
                fetch('/hits')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('count').textContent = data.hits;
                })
                .catch(error => {
                    console.error('Error fetching hits:', error);
                });
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html, count=count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
