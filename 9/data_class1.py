import dataclasses

@dataclasses.dataclass(frozen=True)
class Person:
    firstname: str
    lastname: str
    age: int = 0

    def show(self):
        print(f'私の名前は{self.lastname}{self.firstname}です！ ')

if __name__ == '__main__':
    p1 = Person('太郎', '山田', 58)
    p2 = Person('太郎', '山田', 58)
    print(p1) # 結果：Person(firstname='太郎', lastname='山田', age=58)
    print(p1 == p2) # 結果：True
