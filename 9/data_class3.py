import dataclasses

@dataclasses.dataclass(frozen=True)
class Person:
    firstname: str
    lastname: str
    age: int = 0
    memos: list = dataclasses.field(default_factory=list)

ms = ['married', 'AB']
p = Person('太郎', '山田', 58, ms)
# 初期化メソッドに渡したオブジェクトを変更
ms.append('dog')
print(p)
    # 結果：Person(firstname='太郎', lastname='山田', age=58, memos=['married', 'AB', 'dog'])

p = Person('太郎', '山田', 58, ['married', 'AB'])
# フィールド経由で取得したオブジェクトを変更
p.memos.append('dog')
print(p)
    # 結果：Person(firstname='太郎', lastname='山田', age=58, memos=['married', 'AB', 'dog'])
