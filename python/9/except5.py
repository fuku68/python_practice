# finally節の実行順序
try:
     raise Exception('例外発生')
 except Exception as ex:
     print(ex.args[0])
finally:
    print('**Finally**')


def hoge():
    try:
        return 'Hoge'
    finally:
        print('**Finally**')

print('Start')
print(hoge())
print('End')
