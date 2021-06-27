sets = {'鈴木', '佐藤', '田中', '山本'}
print(sets) # 結果：{'佐藤', '鈴木', '田中', '山本'}

sets2 = set(['山田', '林', '本多', '山田'])
print(sets2) # 結果：{'本多', '林', '山田'}

sets3 = {'鈴木', '山田', frozenset(['山田', '小杉'])}
print(sets3) # 結果：{frozenset({'小杉', '山田'}), '鈴木', '山田'}


sets = {'鈴木', '佐藤', '田中', '山本'}
sets.add('伊藤')
sets.add('田中')
print(sets)

sets.remove('山本')

for item in sets:
    print(item) # 結果：鈴木、田中、佐藤、伊藤

print(sets.pop())
print(sets)
sets.clear()
print(sets)
