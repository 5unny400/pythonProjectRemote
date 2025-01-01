import time


now = time.localtime()
now = time.strftime("%Y-%m-%d %H:%M:%S", now)
print(now)
print(type(now))

from datetime import datetime
now2 = datetime.now()
now2 = now2.strftime("%Y-%m-%d %H:%M:%S")
print(now2)
print(type(now2))
now3 = datetime.strptime(now2, "%Y-%m-%d %H:%M:%S")
print(now3)
print(type(now3))


stamp3 = now3.timestamp()
stamp4 = time.mktime(now3.timetuple())
print(stamp3)
print(stamp4)

time3 = datetime.fromtimestamp(stamp3)
time4 = datetime.fromtimestamp(stamp4)
print(time3)
print(time4)

from datetime import timedelta
cal_time = time3 + timedelta(hours=1)
print(cal_time)