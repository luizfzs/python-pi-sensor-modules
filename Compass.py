#!/usr/bin/python
import smbus
import time
import math

class Compass:

  bus = smbus.SMBus(1)
  address = 0

  def __init__(self, address):
    self.address = address

  def read_byte(self, adr):
    return self.bus.read_byte_data(self.address, adr)

  def read_word(self, adr):
    high = self.bus.read_byte_data(self.address, adr)
    low = self.bus.read_byte_data(self.address, adr+1)
    val = (high << 8) + low
    return val

  def read_word_2c(self, adr):
    val = self.read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

  def write_byte(self, adr, value):
    self.bus.write_byte_data(self.address, adr, value)

  def getOrientation(self):
    self.write_byte(0, 0b01110000) # Set to 8 samples @ 15Hz
    self.write_byte(1, 0b00100000) # 1.3 gain LSb / Gauss 1090 (default)
    self.write_byte(2, 0b00000000) # Continuous sampling

    scale = 0.92

    x_offset = 46
    y_offset = -117
    x_out = (self.read_word_2c(3) - x_offset) * scale
    y_out = (self.read_word_2c(7) - y_offset) * scale
    z_out = (self.read_word_2c(5)) * scale

    bearing  = math.atan2(y_out, x_out) 
    if (bearing < 0):
      bearing += 2 * math.pi

    return math.degrees(bearing)
