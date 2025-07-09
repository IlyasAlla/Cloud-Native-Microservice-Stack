from flask import Flask
import os
app = Flask(__name__)
@app.route('/')
def hello():
    return f"Hello from API! Connected to {os.environ.get('MONGO_HOST')}"
