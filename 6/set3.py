sets1 = {1, 20, 30, 60, 10, 15}
sets2 = {10, 15, 30}
sets3 = {20, 40, 60}

print(sets1.union(sets2))                # 結果：{1, 10, 15, 20, 60, 30}
print(sets1.union(sets2, sets3))         # 結果：{1, 40, 10, 15, 20, 60, 30}
print(sets1.intersection(sets2))         # 結果：{10, 30, 15}
print(sets1.intersection(sets2, sets3))  # 結果：set()
print(sets1.difference(sets3))           # 結果：{1, 10, 30, 15}
print(sets1.difference(sets2, sets3))    # 結果：{1}
print(sets1.symmetric_difference(sets3)) # 結果：{1, 40, 10, 15, 30}

print(sets1 | sets2)
print(sets1 | sets2 | sets3)
print(sets1 & sets2)
print(sets1 & sets2 & sets3)
print(sets1 - sets3)
print(sets1 - sets2 - sets3)
print(sets1 ^ sets3)
