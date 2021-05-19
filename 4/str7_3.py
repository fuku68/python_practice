print('{}は{}、{}歳です。'.format('サクラ', '女の子', 2))
# 結果：サクラは女の子、2歳です。

print('{0}は{2}歳、{1}です。'.format('サクラ', '女の子', 2))
 # 結果：サクラは2歳、女の子です。

print('{name}は{age}歳、{sex}です。'.format(
    name = 'サクラ', sex = '女の子', age = 2))
    # 結果：サクラは2歳、女の子です。

name = 'サクラ'
sex = '女の子'
age = 2
print(f'{name}は{sex}、{age}歳です。')
    # 結果：サクラは女の子、2歳です。
print(f'{name=}は{sex=}、{age=}歳です。')
    # 結果：name='サクラ'はsex='女の子'、age=2歳です。
