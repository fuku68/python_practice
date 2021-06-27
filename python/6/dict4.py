d = {'apple': 'りんご', 'orange': 'みかん', 'melon': 'メロン'}

# 項目を列挙
for item in d.items():
    print(item)
# 結果：('apple', 'りんご')
# ('orange', 'みかん')
# ('melon', 'メロン')


for key, value in d.items():
    print(key, ':', value)
# 結果：apple : りんご
# orange : みかん
# melon : メロン


# キーを列挙
for key in d.keys():
    print(key)


# 値を列挙
for value in d.values():
    print(value)


values = d.values()
d['apple'] = '林檎'

for value in values:
    print(value)
# 結果：林檎
# みかん
# メロン
