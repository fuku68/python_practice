l = [1, 3, 5, 1]
l.remove(1)
print(l)
l.clear()
print(l)


l = [1, 2, 3, 4, 5]
l[2:2] = [6, 7, 8]
print(l)
l[4:6] = [9, 10]
print(l)
l[3:7] = []
print(l)


l = [1, 2, 3, 4, 5]
l.index(5)
# ERROR
l.index(6)
6 in l
