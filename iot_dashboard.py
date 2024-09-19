import RPi.GPIO as GPIO
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Setup GPIO
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Function to control LED
def control_led(state):
    if state == 'on':
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN,GPIO.LOW)

@app.route('/')
def index():
    # Load the web interface
    return render_template('index.html')

@app.route('/led_control', methods=['POST'])
def led_control():
    data = request.json
    led_state = data['led']
    control_led(led_state)
    return jsonify(success=True, state=led_state)

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5500, debug=True)
    except KeyboardInterrupt:
        GPIO.cleanup()
