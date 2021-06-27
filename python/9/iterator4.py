import math

class Prime:
    def __init__(self, max):
        self.max = max
        self.__current = 1

    # イテレーター（自分自身を返す）
    def __iter__(self):
        return self

    # イテレーターの本体を実装
    def __next__(self):
        while True:
            self.__current += 1
            if self.__current > self.max:
                 raise StopIteration
            elif self.__is_prime(self.__current):
                return self.__current

    # 引数valueが素数かどうかを判定
    def __is_prime(self, value):
        result = True # 素数かどうかを表すフラグ
        # 2 ～ sqrt(value)で、valueを割り切れる（＝余りが0）ものがあるか
        for i in range(2, math.floor(math.sqrt(value)) + 1):
            if value % i == 0:
                result = False # 割り切れるものがあれば素数でない
                break
        return result

if __name__ == '__main__':
    pr = Prime(100)
    for p in pr:
        print(p)
