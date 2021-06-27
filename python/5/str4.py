msg = 'にわにはにわにわとりがいる'

print(msg.find('にわ'))         # 結果：0
print(msg.find('にも'))         # 結果：-1
print(msg.rfind('にわ'))        # 結果：6 
print(msg.find('にわ', 3))      # 結果：4
print(msg.find('にわ', 3, 5))   # 結果：-1
print(msg.find('にわ', -7, -1)) # 結果：6

print(msg.count('にわ'))        # 結果：3
print(msg.count('にわ', 3))     # 結果：2
print(msg.count('にわ', 3, 6))  # 結果：1

msg = 'いちいちいちばにいち'
print(msg.count('いちいち'))    # 結果：1
