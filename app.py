from flask import Flask
from flask import render_template
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7,True)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11,True)
GPIO.setup(15, GPIO.OUT)
GPIO.output(15,True)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led/<action>')
def led(action):
    if action == 'off':
        off()
    elif action == 'red':
        red()
    elif action == 'green':
        green()
    elif action == 'blue':
        blue()
    return 'OK %s' % action

def off():
    GPIO.output(15,True)
    GPIO.output(11,True)
    GPIO.output(7,True)

def red():
    GPIO.output(15,False)
    GPIO.output(11,True)
    GPIO.output(7,True)

def green():
    GPIO.output(15,True)
    GPIO.output(11,False)
    GPIO.output(7,True)

def blue():
    GPIO.output(15,True)
    GPIO.output(11,True)
    GPIO.output(7,False)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

GPIO.cleanup()
