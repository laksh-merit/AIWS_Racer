from board import SCL, SDA
import busio
import time

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685

# Create the I2C bus interface.
i2c_bus = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c_bus)

# Set the PWM frequency to 60hz.
pca.frequency = 60

# Set the PWM duty cycle for channel zero to 50%. duty_cycle is 16 bits to match other PWM objects
# but the PCA9685 will only actually give 12 bits of resolution.
while True:
#forward  65536
     pca.channels[4].duty_cycle = 0x2AF8
     pca.channels[5].duty_cycle = 0
     pca.channels[6].duty_cycle = 0
     pca.channels[7].duty_cycle = 0x2AF8
     time.sleep(2)


     pca.channels[4].duty_cycle = 0
     pca.channels[5].duty_cycle = 0
     pca.channels[6].duty_cycle = 0
     pca.channels[7].duty_cycle = 0
     time.sleep(2)


