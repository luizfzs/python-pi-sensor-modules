from HCSR04 import HCSR04
import time

sensor = HCSR04(11, 13)
print "Measuring with mean of 5 samples"
s = time.time()
distance = sensor.measure(5)
e = time.time()

print "Distance: ", distance, " cm"
print "Used time: ",(e - s), " seconds"
