import math

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __int__(self):
        return int(self.__float__())

    def __float__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

if __name__ == '__main__':
    c = Coordinate(1, 2)
    print(float(c)) # 結果：2.23606797749979
    print(int(c)) # 結果：2
