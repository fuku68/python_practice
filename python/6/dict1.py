d1 = {'red': '赤', 'white': '白', 'yellow': '黄'}
print(d1) # 結果：{'red': '赤', 'white': '白', 'yellow': '黄'}

d2 = {}
print(d2) # 結果：{}

d3 = dict(red='赤', white='白', yellow='黄')
print(d3) # 結果：{'red': '赤', 'white': '白', 'yellow': '黄'}

d4 = dict([('red', '赤'), ('white', '白'), ('yellow', '黄')])
print(d4) # 結果：{'red': '赤', 'white': '白', 'yellow': '黄'}

d5 = dict({'yellow': '黄', 'white': '白', 'red': '赤'})
print(d5) # 結果：{'yellow': '黄', 'white': '白', 'red': '赤'}

d6 = dict({'red': '赤', 'white': '白', 'yellow': '黄'},
            white='しろ', black='黒')
print(d6)
# 結果：{'red': '赤', 'white': 'しろ', 'yellow': '黄', 'black': '黒'}

d7 = dict(zip(['red', 'white', 'yellow'], ['赤', '白', '黄']))
print(d7) # 結果：{'red': '赤', 'white': '白', 'yellow': '黄'}
