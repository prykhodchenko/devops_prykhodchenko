#!/usr/bin/env python3
import string

from typing import Dict

from type_aliases import PasswordValidationResult


class PasswordValidator:
    __password_validation_result: PasswordValidationResult = {
        'password_length': False,
        'punctuation': False,
        'upper_case_char': False,
        'lower_case_char': False,
        'digit': False
    }
    __is_password_valid: bool = False
    __password: str = ''

    def __init__(self, password: str) -> None:
        self.__password = password


    @property
    def password_validation_result(self) -> PasswordValidationResult:
        return self.__password_validation_result

    @property
    def is_password_valid(self) -> bool:
        return self.__is_password_valid

    @classmethod
    def validate_password(cls) -> bool:
        cls.__password_validation_result['password_length'] = len(cls.__password) >= 8

        for i in cls.__password:
            if i in string.punctuation:
                cls.__password_validation_result['punctuation'] = True
            elif i.isupper():
                cls.__password_validation_result['upper_case_char'] = True
            elif i.islower():
                cls.__password_validation_result['lower_case_char'] = True
            elif i.isdigit():
                cls.__password_validation_result['digit'] = True

        cls.__is_password_valid = all(bool(password_validation_result) is True for password_validation_result in
                                       cls.__password_validation_result.values())

        return cls.__is_password_valid
