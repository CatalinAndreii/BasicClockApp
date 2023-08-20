# current time program
import time
from time import gmtime, strftime
currentTime = time.time()
clock = strftime("%a, %d %b %Y %H:%M:%S", gmtime(currentTime))
print(clock)
