class Top:
    def hoge(self):
        print('TopA')

class MiddleA(Top):
    def hoge(self):
        print('MiddleA')

class MiddleB(Top):
    def hoge(self):
        print('MiddleB')

# MiddleA ／ Bクラスを多重継承
class Low(MiddleA, MiddleB):
    pass

if __name__ == '__main__':
    l = Low()
    l.hoge() # 結果：MiddleA

    print(Low.mro())
