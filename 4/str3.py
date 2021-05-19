import unicodedata

print(unicodedata.digit('５'))     # 結果：5
print(unicodedata.numeric('参'))    # 結果：3.0
print(unicodedata.numeric('Ⅷ'))    # 結果：8.0


import keyword

id1 = 'tiff'
id2 = 'if'

print(id1.isidentifier())       # 結果：True
print(id2.isidentifier())       # 結果：True
print(keyword.iskeyword(id1))   # 結果：False
print(keyword.iskeyword(id2))   # 結果：True
