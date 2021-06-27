# enumerate
data = ['ぱんだ', 'うさぎ', 'こあら', 'とら']

for index, value in enumerate(data):
    print(index, ':', value)

# zip
data1 = ['ぱんだ', 'うさぎ', 'こあら', 'とら']
data2 = ['panda', 'rabbit', 'koala']

for d1, d2 in zip(data1, data2):
    print(d1, '=', d2)

# all
l = [2, 4, 6]
print(all([i % 2 == 0 for i in l]))
