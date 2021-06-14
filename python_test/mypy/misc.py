import sys
import re
from typing import Match, IO, Optional

# "typing.Match" describes regex matches from the re module
x: Optional[Match[str]] = re.match(r'[0-9]+', "15")

# Use IO[] for functions that should accept or return any
# object that comes from an open() call (IO[] does not
# distinguish between reading, writing or other modes)
def get_sys_IO(mode: str = 'w') -> IO[str]:
    if mode == 'w':
        return sys.stdout
    elif mode == 'r':
        return sys.stdin
    else:
        return sys.stdout

# Forward references are useful if you want to reference a class before
# it is defined
def f(foo: A) -> int:  # This will fail
    ...

class A:
    pass
