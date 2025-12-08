from flask import Flask
# No need to import os or threading, Gunicorn handles the running

# Create the Flask application instance
app = Flask(__name__)

# Define the health check route
@app.route('/')
def home():
    # This response prevents the "No open ports detected" timeout
    return "Telegram Bot Long Polling Active", 200