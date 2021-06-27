data = [1, 2, 3]
itr = iter(data)
print(next(itr)) # 結果：1
print(next(itr)) # 結果：2
print(next(itr)) # 結果：3
print(next(itr)) # 結果：StopIteration
