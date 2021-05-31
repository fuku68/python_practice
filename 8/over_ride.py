class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def show(self):
        print(f'私の名前は{self.lastname}{self.firstname}です！ ')

# Personを継承したBusinessPersonクラスを定義
class BusinessPerson(Person):
    def work(self):
        print(f'{self.lastname}{self.firstname}は働いています。')

class EliteBusinessPerson(BusinessPerson):
    def work(self):
        print(f'{self.lastname}{self.firstname}はバリバリ働いています。')

if __name__ == '__main__':
    bp = EliteBusinessPerson('太郎', '山田')
    bp.work() # 結果：山田太郎はバリバリ働いています。
    bp.show() # 結果：私の名前は山田太郎です！
