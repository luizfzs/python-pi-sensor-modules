#=====================================#
# Author: Luiz Felipe Zafra Saggioro  #
# Created: 21/02/2015                 #
#=====================================#

from WheelEncoder import WheelEncoder
import time


sensor = WheelEncoder(3, 10, 3)
while(True):

  dist = sensor.getCurrentDistance()
  print "Distance: ",dist,"cm"
  print "Ticks: ",sensor.getTicks()
  time.sleep(0.01)
