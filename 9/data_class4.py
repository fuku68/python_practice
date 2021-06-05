import dataclasses

@dataclasses.dataclass()
class Person:
    firstname: str
    lastname: str

if __name__ == '__main__':
    for f in dataclasses.fields(Person):
        print(f)

    p = Person('次郎', '山田')
    print(dataclasses.asdict(p))
    print(dataclasses.astuple(p))

    p2 = dataclasses.replace(p, firstname='太郎')
    print(p)
    print(p2)
