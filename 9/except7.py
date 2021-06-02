# アプリ独自例外の基底クラス
class MyAppError(Exception):
    pass

# アプリ独自例外の個別クラス
class MyInputError(MyAppError):
    def __init__(self, code, message):
        self.code = code
        self.message = message

if __name__ == '__main__':
    try:
        raise MyInputError(501, 'Invalid Input')
    except MyAppError as ex:
        print(ex.args) # 結果：(501, 'Invalid Input')
