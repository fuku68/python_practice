class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    # インスタンス変数の内容を出力
    def show(self):
        print(f'私の名前は{self.lastname}{self.firstname}です！ ')

def show_first(self):
    print(f'名前は{self.firstname}です！ ')

Person.show_first = show_first

p1 = Person('太郎', '山田')
p2 = Person('花子', '鈴木')

p1.show_first()
p2.show_first()
