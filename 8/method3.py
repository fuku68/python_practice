import types

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    # インスタンス変数の内容を出力
    def show(self):
        print(f'私の名前は{self.lastname}{self.firstname}です！ ')

def show_last(self):
    print(f'苗字は{self.lastname}です！ ')

p1 = Person('太郎', '山田')
p2 = Person('花子', '鈴木')
p1.show_last = types.MethodType(show_last, p1)

p1.show_last()
p2.show_last()
