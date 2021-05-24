d = {'apple': 'りんご', 'orange': 'みかん', 'melon': 'メロン'}
result = {value: key for key, value in d.items()}
print(result) # 結果：{'りんご': 'apple', 'みかん': 'orange', 'メロン': 'melon'}


data = ['apple', 'orange', 'melon', 'pear', 'olive']
result = {item[0]: item for item in data}
print(result) # 結果：{'a': 'apple', 'o': 'olive', 'm': 'melon', 'p': 'pear'}
