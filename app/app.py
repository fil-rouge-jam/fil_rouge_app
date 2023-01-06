import os
from flask import Flask
from redis import Redis

redis = Redis(host=os.getenv('REDIS_HOST', 'localhost'),
              port=os.getenv('REDIS_PORT', '6379'))
app = Flask(__name__)


@app.route('/')
def hello():
    """
    Hello method at / API endpoint to greet user and return number of visit
    """
    return "Hello"

@app.route('/health')
def health():
    """
    Healthcheck method at /health to allow kubernetes healthcheck
    """
    return "ok"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
