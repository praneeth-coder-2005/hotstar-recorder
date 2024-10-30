from flask import Flask
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

app = Flask(__name__)

@app.route('/start_recording')
def start_recording():
    # Your login and recording logic
    print("Recording Started")  # Add real recording logic here
    return "Recording Started"

@app.route('/stop_recording')
def stop_recording():
    # Code to stop the recording
    print("Recording Stopped")  # Add real stopping logic here
    return "Recording Stopped"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
