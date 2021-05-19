msg = 'WINGSプロジェクト'

print('プロ' in msg)                # 結果：True
print('プロ' not in msg)            # 結果：False
print(msg.startswith('WINGS'))      # 結果：True
print(msg.endswith('WINGS'))        # 結果：False
print(not msg.startswith('WINGS'))  # 結果：False
print(msg.startswith('WINGS', 1))   # 結果：False
print('プロ' in msg[6:])            # 結果：False
print('wings' in msg)               # 結果：False
print('wings' in msg.casefold())    # 結果：True
