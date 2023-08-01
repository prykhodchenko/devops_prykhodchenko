#!/usr/bin/env python3

import string
import random
import numpy as np
from typing import List


class PasswordGenerator:
    __password_length: int = 8
    __uppercase_letters: bool = False
    __lowercase_letters: bool = False
    __digits: bool = False
    __punctuation: bool = False
    __password: str or None = None

    def __init__(self, password_length, uppercase_letters, lowercase_letters, digits, punctuation) -> None:
        self.__password_length: int = password_length
        self.__uppercase_letters: bool = uppercase_letters
        self.__lowercase_letters: bool = lowercase_letters
        self.__digits: bool = digits
        self.__punctuation: bool = punctuation

    @property
    def password(self) -> str:
        return self.__password

    @staticmethod
    def get_required_characters() -> List[str]:
        return [
            random.choices(string.ascii_uppercase, weights=None, k=1)[0],
            random.choices(string.ascii_lowercase, weights=None, k=1)[0],
            random.choices(string.punctuation, weights=None, k=1)[0],
            random.choices(string.digits, weights=None, k=1)[0],
        ]

    @classmethod
    def generate_password(cls) -> str:
        all_characters: str = string.digits + string.punctuation + string.ascii_lowercase + string.ascii_uppercase
        required_characters: List[str] = PasswordGenerator.get_required_characters()
        password_length_without_required_characters: int = cls.__password_length - len(required_characters)
        random_chose_characters: List[str] = random.choices(all_characters, weights=None,
                                                            k=password_length_without_required_characters)
        password_list: List = list(np.concatenate((random_chose_characters, required_characters)))

        random.shuffle(password_list)

        cls.__password = ''.join(str(x) for x in password_list)

        return cls.__password
