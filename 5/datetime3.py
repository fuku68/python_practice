import datetime

dt = datetime.datetime.now(datetime.timezone.utc)
print(dt) # 結果：2019-11-18 07:54:15.640504+00:00
print(dt.year) # 結果：2019
print(dt.month) # 結果：11
print(dt.day) # 結果：18
print(dt.hour) # 結果：7
print(dt.minute) # 結果：54
print(dt.second) # 結果：15
print(dt.microsecond) # 結果：640504
print(dt.tzinfo) # 結果：UTC

dt = datetime.datetime.now(datetime.timezone.utc)
print(dt) # 結果：2019-11-18 08:02:25.017604+00:00
print(dt.date()) # 結果：2019-11-18
print(dt.time()) # 結果：08:02:25.017604
print(dt.timetz()) # 結果：08:02:25.017604+00:00
print(dt.timestamp()) # 結果：1574064145.017604
print(dt.toordinal()) # 結果：737381
print(dt.weekday()) # 結果：0
print(dt.isoweekday()) # 結果：1
print(dt.isocalendar()) # 結果：(2019, 47, 1)
