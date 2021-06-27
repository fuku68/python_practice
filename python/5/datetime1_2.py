import datetime

print(datetime.datetime(2019, 12, 4, 15, 35, 58, 469))
    # 結果：2019-12-04 15:35:58.000469
print(datetime.datetime(2019, 12, 4, 15, 35, 58, 469,
    datetime.timezone(datetime.timedelta(hours=9))))
     # 結果：2019-12-04 15:35:58.000469+09:00

print(datetime.date(2019, 12, 4))
    # 結果：2019-12-04
print(datetime.time(15, 35, 58, 469))
    # 結果：15:35:58.000469
print(datetime.time(15, 35, 58, 469,
    datetime.timezone(datetime.timedelta(hours=9))))
    # 結果：15:35:58.000469+09:00

print(datetime.datetime(2019, 13, 4, 15, 35, 58, 469))
    # 結果：エラー（ValueError: month must be in 1..12）
