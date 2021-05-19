import datetime

dt = datetime.datetime.now(datetime.timezone.utc)
# 対応するタイムスタンプ値を取得
ts = dt.timestamp()

print(datetime.datetime.fromtimestamp(ts))
    # 結果：2019-11-18 16:45:55.796894
print(datetime.datetime.fromtimestamp(ts, datetime.timezone.utc))
    # 結果：2019-11-18 07:45:55.796894+00:00
print(datetime.date.fromtimestamp(ts)) # 結果：2019-11-18
