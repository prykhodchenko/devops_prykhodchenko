#!/usr/bin/env python3
import string
from typing import Dict

from type_aliases import PasswordValidationResult


class PasswordValidator:
    __password_validation_requirements: Dict[str, bool] = {}
    __password_validation_result: Dict[str, bool] = {}
    __is_password_valid: bool = False

    def __init__(self, check_password_length=True, check_digit=True, check_punctuation=True, check_upper_case_char=True,
                 check_lower_case_char=True) -> None:
        self.__password_validation_requirements.update({
            'check_password_length': check_password_length,
            'check_digit': check_digit,
            'check_punctuation': check_punctuation,
            'check_upper_case_char': check_upper_case_char,
            'check_lower_case_char': check_lower_case_char
        })

    @property
    def password_validation_result(self) -> PasswordValidationResult:
        return self.__password_validation_result

    @property
    def is_password_valid(self) -> bool:
        return self.__is_password_valid

    @classmethod
    def validate_password(cls, password: str) -> bool:
        if bool(cls.__password_validation_requirements.get('check_password_length')):
            cls.__password_validation_result['password_length'] = len(password) >= 8
        print()
        for i in password:
            if bool(cls.__password_validation_requirements.get('check_punctuation')):
                cls.__password_validation_result['punctuation'] = i in string.punctuation
            if bool(cls.__password_validation_requirements.get('check_upper_case_char')):
                cls.__password_validation_result['upper_case_char'] = i.isupper()
            if bool(cls.__password_validation_requirements.get('check_lower_case_char')):
                cls.__password_validation_result['lower_case_char'] = i.islower()
            if bool(cls.__password_validation_requirements.get('check_digit')):
                cls.__password_validation_result['digit'] = i.isdigit()

        cls.__is_password_valid = all(bool(password_validation_result) is True for password_validation_result in
                                      cls.__password_validation_result.values())

        return cls.__is_password_valid
