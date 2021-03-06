class MyInfo:
    # アトリビュート格納のための__data（辞書）を準備
    def __init__(self):
        super().__setattr__('__data', {})

    # 指定されたアトリビュートを__dataから取得
    def __getattr__(self, name):
        try:
            return super().__getattribute__('__data')[name]
        except KeyError as ex:
            return None

    # 指定されたアトリビュートを__dataに格納
    def __setattr__(self, name, value):
        super().__getattribute__('__data')[name] = value

if __name__ == '__main__':
    i = MyInfo()
    i.score = 58
    i.hobby = '卓球'
    print(i.hobby) # 結果：卓球
    print(i.__dict__) # 結果：{'__data': {'score': 58, 'hobby': '卓球'}}
