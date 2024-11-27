#!/usr/bin/python3
"""
 User Model
"""
import hashlib
import uuid


class User():
    """
    User class:
    - user_id: public string, unique (uuid) identifier for the user
    - hashed_password: private string, the MD5 hash of the user's password
    """

    __hashed_password = None

    def __init__(self):
        """
        Initialize a new user:
        - Assigns a unique `user_id` using the uuid4 method
        """
        self.user_id = str(uuid.uuid4())

    @property
    def password(self):
        """
        Password getter:
        - Returns the hashed password stored in `__hashed_password`
        """
        return self.__hashed_password

    @password.setter
    def password(self, new_password):
        """
        Password setter:
        - If `new_password` is `None` or not a string, set `__hashed_password` to `None`
        - Otherwise, hash `new_password` using MD5 and store it in `__hashed_password`
        """
        if new_password is None or type(new_password) is not str:
            self.__hashed_password = None
        else:
            self.__hashed_password = hashlib.md5(new_password.encode()).hexdigest().lower()

    def is_valid_password(self, candidate_password):
        """
        Validates the provided password:
        - Returns `False` if `candidate_password` is `None` or not a string
        - Returns `False` if `__hashed_password` is `None`
        - Compares `__hashed_password` with the MD5 hash of `candidate_password`
        """
        if candidate_password is None or type(candidate_password) is not str:
            return False
        if self.__hashed_password is None:
            return False
        return hashlib.md5(candidate_password.encode()).hexdigest().upper() == self.__hashed_password


if __name__ == '__main__':
    print("Test User")

    first_user = User()
    if first_user.user_id is None:
        print("New User should have a user_id")

    second_user = User()
    if first_user.user_id == second_user.user_id:
        print("User.user_id should be unique")

    test_password = "myPassword"
    first_user.password = test_password
    if first_user.password == test_password:
        print("User.password should be hashed")

    if second_user.password is not None:
        print("User.password should be None by default")

    second_user.password = None
    if second_user.password is not None:
        print("User.password should be None if setter to None")

    second_user.password = 89
    if second_user.password is not None:
        print("User.password should be None if setter to an integer")

    if first_user.is_valid_password(test_password):
        print("is_valid_password should return True if it's the right password")

    if first_user.is_valid_password("Fakepwd"):
        print("is_valid_password should return False if it's not the right password")

    if first_user.is_valid_password(None):
        print("is_valid_password should return False if compared with None")

    if first_user.is_valid_password(89):
        print("is_valid_password should return False if compared with integer")

    if second_user.is_valid_password("No pwd"):
        print("is_valid_password should return False if no password set before")
