class Area:
    # 円周率を準備
    PI = 3.14

    @classmethod
    def circle(cls, radius):
        return radius * radius * cls.PI

if __name__ == '__main__':
    print(Area.PI)          # 結果：3.14
    print(Area.circle(10))  # 結果：314.0
