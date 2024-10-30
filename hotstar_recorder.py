from flask import Flask
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

app = Flask(__name__)

@app.route('/')  # This route handles requests to the root URL
def home():
    return "Welcome to the Hotstar Recorder!"

@app.route('/start_recording')  # Route to start recording
def start_recording():
    # Your login and recording logic (placeholder for now)
    print("Recording Started")  # Replace with actual recording logic
    return "Recording Started"

@app.route('/stop_recording')  # Route to stop recording
def stop_recording():
    # Code to stop the recording (placeholder for now)
    print("Recording Stopped")  # Replace with actual stopping logic
    return "Recording Stopped"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
