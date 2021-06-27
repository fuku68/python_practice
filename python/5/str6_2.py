data1 = ['いぬ', 'ねこ', 'たぬき']
print(','.join(data1))  # 結果：いぬ,ねこ,たぬき
data2 = [10, 103, 18]
# print('¥t'.join(data2)) # 結果：エラー
print('¥t'.join([str(i) for i in data2]))   # 結果：10  103 18
