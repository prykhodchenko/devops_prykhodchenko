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

    def __init__(self, password: str) -> None:
        self.__password_validation_result['password_length'] = len(password) >= 8

        for i in password:
            if i in string.punctuation:
                self.__password_validation_result['punctuation'] = True
            elif i.isupper():
                self.__password_validation_result['upper_case_char'] = True
            elif i.islower():
                self.__password_validation_result['lower_case_char'] = True
            elif i.isdigit():
                self.__password_validation_result['digit'] = True

        self.__is_password_valid = all(bool(password_validation_result) is True for password_validation_result in
                                       self.__password_validation_result.values())

    @property
    def password_validation_result(self) -> PasswordValidationResult:
        return self.__password_validation_result

    @property
    def is_password_valid(self) -> bool:
        return self.__is_password_valid
