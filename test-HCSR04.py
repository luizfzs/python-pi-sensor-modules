from HCSR04 import HCSR04
import time

samples = 3

sensor = HCSR04(11, 13)
print "Measuring with mean of", samples, "samples"
s = time.time()
distance = sensor.measure(samples, "cm")
e = time.time()
print "Distance:", distance, "cm"
print "Used time:",(e - s), "seconds"

print "Measuring with mean of", samples, "samples"
s = time.time()
distance = sensor.measure(samples, "in")
e = time.time()
print "Distance:", distance, "in"
print "Used time:",(e - s), "seconds"

print "Measuring with mean of", samples, "samples"
s = time.time()
distance = sensor.measure(samples, "ft")
e = time.time()
print "Distance:", distance, "ft"
print "Used time:",(e - s), "seconds"

