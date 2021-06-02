class Person:
    __slots__ = ['__firstname', '__lastname']
    def __init__(self, firstname, lastname):
        self.__firstname = firstname
        self.__lastname = lastname

    # firstname ／ lastnameのゲッターを宣言（読み取り専用）
    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastname

    # del呼び出しを禁止
    def __delattr__(self, name):
        raise RuntimeError

    def __eq__(self, other):
        if isinstance(other, Person):
             return self.firstname == other.firstname and \
                self.lastname == other.lastname
        return False

    # ハッシュ値を演算
    def __hash__(self):
        return hash((self.firstname, self.lastname))

if __name__ == '__main__':
    p = Person('太郎', '山田')
    dic = {p: '男'}
    del p.firstname
    print(dic[p])
