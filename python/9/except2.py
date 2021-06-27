file = None
try:
    file = open('./except1.py', 'r', encoding='UTF-8')
    data = file.read()
    print(data)
finally:
    # ファイルが存在する場合、これを閉じる
    if file:
        file.close()
