import datetime

print(datetime.datetime.today()) # 結果：2020-02-13 09:33:11.988985 
print(datetime.date.today())     # 結果：2020-02-13
print(datetime.datetime.now())  # 結果：2020-02-13 09:33:11.989985
print(datetime.datetime.now( datetime.timezone(datetime.timedelta(hours=9))))
    # 結果：2020-02-13 09:33:11.989985+09:00

print(datetime.datetime.utcnow())
    # 結果：2020-02-13 00:33:11.989985
print(datetime.datetime.now(datetime.timezone.utc))
    # 結果：2020-02-13 00:33:11.990984+00:00
