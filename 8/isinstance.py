class Figure():
    # width（幅）、height（高さ）を準備
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 面積を取得
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
    # Figure派生クラスのリストを準備
    figs = [
        Triangle(10, 15),
        Rectangle(10, 15),
        Triangle(5, 1)
    ]
    # 配列figsの内容を順番に処理
    for fig in figs:
        if isinstance(fig, Figure):
            print(f'{fig.__class__}：{fig.get_area()}')

