import socketio
from board import SCL, SDA
import busio
import time

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
kit.servo[15].angle = 91

# Create the I2C bus interface.
i2c_bus = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c_bus)

# Set the PWM frequency to 60hz.
pca.frequency = 60

sio = socketio.Client()


@sio.event
def connect():
    print('Connection Established...')


@sio.event
def disconnect():
    print('Disconnected...')


@sio.on('message')
def handleMessage(msg):
    print(msg)
    if msg.isalpha():
        if msg == "backward":
            pca.channels[4].duty_cycle = 0
            pca.channels[5].duty_cycle = 0x8000
            pca.channels[6].duty_cycle = 0x8000
            pca.channels[7].duty_cycle = 0

        elif msg == "forward":
            pca.channels[4].duty_cycle = 0x8000
            pca.channels[5].duty_cycle = 0
            pca.channels[6].duty_cycle = 0
            pca.channels[7].duty_cycle = 0x8000

        elif msg == "Stop":
            pca.channels[4].duty_cycle = 0
            pca.channels[5].duty_cycle = 0
            pca.channels[6].duty_cycle = 0
            pca.channels[7].duty_cycle = 0
    else:
        a = int(msg)
        if a > 35 and a < 147:
            kit.servo[15].angle = int(msg)


sio.connect("http://139.59.44.106:5000")
