msg = ' こんにちは ¥t¥n¥r'

print('「' + msg.strip() + '」')    # 結果：「こんにちは」
print('「' + msg.lstrip() + '」')   # 結果：「こんにちは \t\n\r」
print('「' + msg.rstrip() + '」')   # 結果：「 こんにちは」

msg2 = '!======［独習Python］======!'
print('「' + msg2.strip('!=［］') + '」')   # 結果：「独習Python」
