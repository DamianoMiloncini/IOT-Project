import RPi.GPIO as GPIO
from flask import Flask, send_from_directory, request

app = Flask(__name__)

# Setup GPIO
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/turn_on', methods=['POST'])
def turn_on():
    GPIO.output(LED_PIN, GPIO.HIGH)
    return "ON"

@app.route('/turn_off', methods=['POST'])
def turn_off():
    GPIO.output(LED_PIN, GPIO.LOW)
    return "OFF"

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5500, debug=True)
    finally:
        GPIO.cleanup()
