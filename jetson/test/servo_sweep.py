from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

while True:
     for i in range(36,126,1):
          kit.servo[0].angle=i
          time.sleep(0.05)
          print("moving forward")

     for j in range(36,126,1):
          i=i-1
          kit.servo[0].angle=i
          time.sleep(0.05)
          print("moving backward")
