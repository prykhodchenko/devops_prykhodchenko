#!/usr/bin/env python3
import string
from typing import Dict

from type_aliases import PasswordValidationResult


class PasswordValidator:
    __password_validation_requirements: PasswordValidationResult = {}
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
            cls.check_password_length(password)

        if bool(cls.__password_validation_requirements.get('check_digit')):
            cls.check_if_has_digit(password)

        if bool(cls.__password_validation_requirements.get('check_punctuation')):
            cls.check_if_has_punctuation(password)

        if bool(cls.__password_validation_requirements.get('check_upper_case_char')):
            cls.check_if_has_upper_case_char(password)

        if bool(cls.__password_validation_requirements.get('check_lower_case_char')):
            cls.check_if_has_lower_case_char(password)

        cls.__is_password_valid = all(bool(password_validation_result) is True for password_validation_result in
                                      cls.__password_validation_result.values())

        return cls.__is_password_valid

    @classmethod
    def check_password_length(cls, password: str) -> None:
        cls.__password_validation_result['password_length'] = True if len(password) >= 8 else False

    @classmethod
    def check_if_has_digit(cls, password: str) -> None:
        for character in password:
            if character.isdigit():
                cls.__password_validation_result['digit'] = True
                break
            else:
                cls.__password_validation_result['digit'] = False

    @classmethod
    def check_if_has_punctuation(cls, password: str) -> None:
        for character in password:
            if character in string.punctuation:
                cls.__password_validation_result['punctuation'] = True
                break
            else:
                cls.__password_validation_result['punctuation'] = False

    @classmethod
    def check_if_has_upper_case_char(cls, password: str) -> None:
        for character in password:
            if character.isupper():
                cls.__password_validation_result['upper_case_char'] = True
                break
            else:
                cls.__password_validation_result['upper_case_char'] = False

    @classmethod
    def check_if_has_lower_case_char(cls, password: str) -> None:
        for character in password:
            if character.islower():
                cls.__password_validation_result['lower_case_char'] = True
                break
            else:
                cls.__password_validation_result['lower_case_char'] = False
