import os
from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

app = Flask(__name__)

driver = None

def init_driver():
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Ensure GUI is off
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver_path = "/home/render/chromedriver"  # Render provides this path for the WebDriver
    driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

def start_recording(url):
    global driver
    if driver is None:
        init_driver()

    driver.get(url)
    time.sleep(5)  # Wait for the page to load
    # Add more detailed steps to log in and start the video based on Hotstar's website structure

@app.route('/')
def home():
    return "Welcome to the Hotstar Recorder!"

@app.route('/start_recording', methods=['POST'])
def start_recording_route():
    data = request.json
    if 'url' not in data:
        return jsonify({'error': 'URL is required'}), 400
    
    url = data['url']
    start_recording(url)
    
    return jsonify({'status': 'Recording started'})

@app.route('/stop_recording', methods=['POST'])
def stop_recording_route():
    global driver
    if driver:
        driver.quit()
        driver = None
        return jsonify({'status': 'Recording stopped'})
    else:
        return jsonify({'error': 'No recording in progress'}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
