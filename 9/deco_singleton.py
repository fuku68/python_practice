def singleton_deco(cls):
    __instance = None
    # インスタンスを返すファクトリー関数
    def inner(*args, **kwargs):
        nonlocal __instance
        if __instance is None:
            __instance = cls(*args, **kwargs)
        return __instance
    return inner

@singleton_deco
class MyClass:
    pass

if __name__ == '__main__':
    c1 = MyClass()
    c2 = MyClass()
    print(c1 is c2) # 結果：True
