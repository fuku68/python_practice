d = {'apple': 'りんご', 'orange': 'みかん', 'melon': 'メロン'}
print(d['pear']) # 結果：エラー（KeyError: 'pear'）

# 値は未削除
print(d.get('pear', '×'))      # 結果：×
# 値は削除
print(d.pop('melon', '×'))     # 結果：メロン
# LIFO
print(d.popitem()) # 結果：('orange', 'みかん')
print(d) # 結果：{'apple': 'りんご'}


d = {'apple': 'りんご', 'orange': 'みかん', 'melon': 'メロン'}
print('orange' in d) # 結果：True
print('pear' in d) # 結果：False


d = {'apple': 'りんご', 'orange': 'みかん', 'melon': 'メロン'}
del d['orange']
print(d)    # 結果：{'apple': 'りんご', 'melon': 'メロン'}
d.clear()
print(d)    # 結果：{}
