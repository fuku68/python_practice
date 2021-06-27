class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    # ハッシュ値を演算
    def __hash__(self):
        return hash((self.firstname, self.lastname))

if __name__ == '__main__':
    p = Person('太郎', '山田')
    dic = {p: '男'}
    p.firstname = '次郎'
    print(dic[p])
