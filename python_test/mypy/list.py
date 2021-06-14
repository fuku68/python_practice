from typing import List  # Python 3.8 and earlier

def greet_all(names: List[str]) -> None:
    for name in names:
        print('Hello ' + name)
