# ディスクリプターの定義
class LogProp:
    # 対象のアトリビュート名（name）を設定
    def __init__(self, name):
        self.name = name

    # アトリビュート取得時の処理
    def __get__(self, obj, type):
        print(f'{self.name}: get')
        return obj.__dict__[self.name]

    # アトリビュート設定時の処理
    def __set__(self, obj, value):
        print(f'{self.name}: set {value}')
        obj.__dict__[self.name] = value

class App:
    # ディスクリプターを定義
    title = LogProp('title')

if __name__ == '__main__':
    app = App()
    app.title = '独習Python'
    print(app.title)
