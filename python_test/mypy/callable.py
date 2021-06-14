from typing import Callable

def twice(i: int, next: Callable[[int], int]) -> int:
    return next(next(i))

def add(i: int) -> int:
    return i + 1

print(twice(3, add))   # 5

# (*args: Any, **kwargs: Any)
def arbitrary_call(f: Callable[..., int]) -> int:
    return f('x') + f(y=2)  # OK

arbitrary_call(len)   # No static error, but fails at runtime
