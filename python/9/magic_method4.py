class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    # 氏／名ともに等しければ同値とする
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.firstname == other.firstname and \
                self.lastname == other.lastname
        return False

class BusinessPerson(Person):
    def __init__(self, firstname, lastname, title):
        super().__init__(firstname, lastname)
        # titleを追加
        self.title = title

    def __eq__(self, other):
        if isinstance(other, BusinessPerson):
            # Person型の判定に加えて、titleも判定
            return super().__eq__(other) and \
                self.title == other.title
        return False

if __name__ == '__main__':
    p = Person('太郎', '山田')
    bp = BusinessPerson('太郎', '山田', '部長')
    # 左辺右辺いずれに位置するにも関わらず、派生クラスの_ _eq_ _メソッドによって同値判定
    print(p == bp) # 結果：True
    print(bp == p) # 結果：True
