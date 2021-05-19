import datetime
import locale

locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')

dt = datetime.datetime(2019, 12, 4, 15, 35, 58, 469)
print(dt) # 結果：2019-12-04 15:35:58.000469
print(dt.strftime('%c')) # 結果：2019/12/04 15:35:58
print(dt.strftime('%x')) # 結果：2019/12/04
print(dt.strftime('%X')) # 結果：15:35:58
print(dt.strftime('%Y年 %m月 %d日（%a） %I時 %M分'))
    # 結果：2019年 12月 04日（水） 03時 35分
