import sys
import time
import datetime


print(time.localtime())
print(time.gmtime().tm_mon)
print(datetime.datetime.now())

#pause for time in seconds
time.sleep(10)

print('Hello World')

sys.exit(1)

