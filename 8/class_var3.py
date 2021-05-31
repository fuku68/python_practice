class Area:
    PI = 3.14

if __name__ == '__main__':
    a = Area()
    print(a.PI) # 結果：3.14

    a.PI = 3.1415926535
    print(a.PI)     # 結果：3.1415926535 
    print(Area.PI)  # 結果：3.14
