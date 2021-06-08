from typing import TypeVar, Type

class User:
    # Defines fields like name, email
    pass

class BasicUser(User):
    def upgrade(self):
        """Upgrade to Pro"""
        pass

class ProUser(User):
    def pay(self):
        """Pay bill"""
        pass

U = TypeVar('U', bound=User)

def new_user(user_class: Type[U]) -> U:
    # Same  implementation as before
    return user_class()

beginner = new_user(BasicUser)  # Inferred type is BasicUser
beginner.upgrade()  # OK
