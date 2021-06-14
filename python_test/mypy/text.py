from typing import Text, AnyStr

def unicode_only(s: Text) -> Text:
    return s + u'\u2713'


def concat(x: AnyStr, y: AnyStr) -> AnyStr:
    return x + y

concat('foo', 'foo')     # Okay
concat(b'foo', b'foo')   # Okay
# concat('foo', b'foo')    # Error: cannot mix bytes and unicode
