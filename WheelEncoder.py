#=====================================#
# Author: Luiz Felipe Zafra Saggioro  #
# Created: 21/02/2015                 #
#=====================================#

import RPi.GPIO as gpio

class WheelEncoder:
  'Encapsulates the attributes and methods to use a wheel encoder sensor'

  inputPin = 0
  ticks = 0
  accTicks = 0
  ticksPerTurn = 0
  radius = 0.0
  distPerTick = 0.0
  PI = 3.1415

  def __init__(self, inputPin, ticksPerTurn, radius):
    self.inputPin = inputPin
    self.ticksPerTurn = ticksPerTurn
    self.radius = radius

    self.setDistPerTick(self.ticksPerTurn, self.radius)

    gpio.setmode(gpio.BOARD)
    gpio.setup(self.inputPin, gpio.IN, pull_up_down=gpio.PUD_UP)
    gpio.add_event_detect(self.inputPin, gpio.FALLING, callback=self.my_callback)

  def getTicks(self):
    return self.ticks

  def resetTicks(self):
    self.ticks = 0

  def getTicksPerTurn(self):
    return self.ticksPerTurn

  def setTicksPerTurn(self, ticks):
    self.ticksPerTurn = ticks

  def getRadius(self):
    return self.radius

  def setRadius(self, rad):
    self.radius = rad

  def setDistPerTick(self, ticksPerTurn, radius):
    self.distPerTick = ( 2 * self.PI * radius ) / ticksPerTurn

  def getCurrentDistance(self):
    return self.ticks * self.distPerTick

  def getTotalDistance(self):
    return self.accTicks * self.distPerTick

  def my_callback(self, channel):
    self.ticks += 1
    self.accTicks += 1

  def getTicksPerDistance(self, dist):
    return (dist / self.distPerTick)
