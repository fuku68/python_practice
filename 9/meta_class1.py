# クラス定義に関わるメソッド（関数）を準備
def init(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname

def show(self):
    print(f'私の名前は{self.lastname}{self.firstname}です！ ')

# Personクラスを定義
Person = type(
    'Person',
    (object, ),
    {
        '__init__': init,
        'show': show
    }
)

if __name__ == '__main__':
    p = Person('太郎', '山田')
    p.show()    # 結果：私の名前は山田太郎です！
