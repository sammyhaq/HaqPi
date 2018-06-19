"""
MPU6050.py
Code by Sammy Haq
https://github.com/sammyhaq

Class for operating the MPU6050 accelerometer/gyro chip.

"""

import smbus
import math
import time


"""
MPU6050 registers and addresses.
"""
PWR_MGMT_1 = 0x6b
PWR_MGMT_2 = 0x6c


ACCEL_XOUT_H = 0x3b
ACCEL_XOUT_L = 0x3c

ACCEL_YOUT_H = 0x3d
ACCEL_YOUT_L = 0x3e

ACCEL_ZOUT_H = 0x3f
ACCEL_ZOUT_L = 0x40


TEMP_OUT_H = 0x41
TEMP_OUT_L = 0x42


GYRO_XOUT_H = 0x43
GYRO_XOUT_L = 0x44

GYRO_YOUT_H = 0x45
GYRO_YOUT_L = 0x46

GYRO_ZOUT_H = 0x47
GYRO_ZOUT_L = 0x48


SMPLRT_DIV = 0x19
CONFIG = 0x1a

WHO_AM_I_MPU6050 = 0x75  # should return 0x68 if visible.

# In older raspberry pi's, you may have to put 0 as the arg instead
bus = smbus.SMBus(1)


class MPU6050:

    # Constructor.
    def __init__(self, address):

        # use i2cdetect -y 1 to find the address of the chip.
        # Example: for me, it's usually 0x68.
        self.address = address

        # ensures power wakeup from sleep
        bus.write_byte_data(address, PWR_MGMT_1, 0)
        # delays sample rate to avoid noise
        bus.write_byte_data(address, SMPLRT_DIV, 7)
        bus.write_byte_data(address, CONFIG, 0)  # disables DLPF.

    def read_raw_data(self, addr):
        high = bus.read_byte_data(self.address, addr)
        low = bus.read_byte_data(self.address, addr+1)

        value = ((high << 8) | low)

        # getting signed value
        if (value > 32768):
            value = value - (32768 * 2)

        return value

    # Gets the corresponding raw data, converts it, rounds to the nearest
    # decimal place, and then returns.

    def getAccel_X(self, decimal):
        return round((self.read_raw_data(ACCEL_XOUT_H)/16384.0), decimal)

    def getAccel_Y(self, decimal):
        return round((self.read_raw_data(ACCEL_YOUT_H)/16384.0), decimal)

    def getAccel_Z(self, decimal):
        return round((self.read_raw_data(ACCEL_ZOUT_H)/16384.0), decimal)

    def getGyro_X(self, decimal):
        return round((self.read_raw_data(GYRO_XOUT_H)/16384.0), decimal)

    def getGyro_Y(self, decimal):
        return round((self.read_raw_data(GYRO_YOUT_H)/16384.0), decimal)

    def getGyro_Z(self, decimal):
        return round((self.read_raw_data(GYRO_ZOUT_H)/16384.0), decimal)

    def getTemp(self, decimal):
        return round((self.read_raw_data(((float)TEMP_OUT_H)/340.00) + 36.53))

    # returns the acceleration data as a formatted, printable string.

    def acceleration_toString(self, decimal):

        ax = self.getAccel_X(decimal)
        ay = self.getAccel_Y(decimal)
        az = self.getAccel_Z(decimal)

        toReturn = 'a_x: {0}, a_y: {1}, a_z: {2}'.format(ax, ay, az)

        return toReturn
