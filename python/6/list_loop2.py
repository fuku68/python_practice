# map
data = [1, 3, 5]
result = map(lambda v: v * v, data)
print(list(result)) # 結果：[1, 9, 25]


data = [1, 3, 5]
data2 = [2, 7, 10]
result = map(lambda v1, v2: v1 * v2, data, data2)
print(list(result)) # 結果：[2, 21, 50]

# filter
data = [
    'フレンチブルドッグ',
    'ヨークシャーテリア',
    'ダックスフント',
    'ポメラニアン',
    'コーギー ',
]
result = filter(lambda v: len(v) < 8, data)
print(list(result)) # 結果：['ダックスフント', 'ポメラニアン', 'コーギー ']

result = [x for x in data if len(x) < 8]
print(result)
