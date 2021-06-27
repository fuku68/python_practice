data = [
    [1, 2, 4],
    [5, 7, 9],
]

data2 = data.copy()
data2[0][1] = 100
print(data)
print(data2)


import copy
data2 = copy.deepcopy(data)
data2[0][0] = 100
print(data)
