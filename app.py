import redis
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)  # connects to Redis container

# Route to get hit count as JSON (for AJAX)
@app.route('/hits')
def get_hits():
    count = r.get('hits')
    count = int(count) if count else 0
    return jsonify(hits=count)

# Main route serves HTML page
@app.route('/')
def hello():
    # increment the hit count
    r.incr('hits')
    count = r.get('hits')
    count = int(count) if count else 0
    
    # Simple HTML template with JavaScript
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
    app.run(host='0.0.0.0', port=5000)
