class Person:
    ADULT = 20

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def show(self):
        print(f' 私の名前は {self.lastname}{self.firstname} です！ ')

    @classmethod
    def is_adult_year(cls, age):
        return age >= cls.ADULT
