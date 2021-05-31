class Figure():
    # width（幅）、height（高さ）を準備
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 面積を取得（中身はダミー）
    @abstractmethod
    def get_area(self):
        pass


class Triangle(Figure):
    # 三角形の面積を求めるためのget_areaメソッドを定義
    def get_area(self):
        return self.width * self.height / 2

class Rectangle(Figure):
    # 四角形の面積を求めるためのget_areaメソッドを定義
    def get_area(self):
        return self.width * self.height


if __name__ == '__main__':
    t = Triangle(10, 15)
    r = Rectangle(10, 15)
    #print(t.get_area()) # 結果：75.0
    print(r.get_area()) # 結果：150
