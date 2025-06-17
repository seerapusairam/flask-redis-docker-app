FROM python:3.10-slim

WORKDIR /app1

COPY req.txt .
RUN pip install -r req.txt

COPY . .

CMD ["python", "app.py"]