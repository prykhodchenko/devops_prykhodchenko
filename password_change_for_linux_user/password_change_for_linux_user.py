#!/usr/bin/env python3

import getpass
from typing import Dict
from colorama import Fore, Style

from user_data_manipulator_on_linux import UserDataManipulatorOnLinux
from password_generator import PasswordGenerator
from password_validator import PasswordValidator


# The initial method of password change
def change_linux_user_password(username: str) -> None:
    typed_password: str = ask_user_to_type_password()

    if typed_password:
        set_typed_password(username, typed_password)
    else:
        set_auto_generated_password(username)


# Method change existing user password on auto-generated password
def set_auto_generated_password(username: str) -> None:
    # ask the user to print the password length.
    password_length: int = ask_password_length()
    password_generator = PasswordGenerator(password_length, True, True, True, True)

    # generate a strong password
    new_password: str = password_generator.password
    password_validator = PasswordValidator(new_password)

    # check password requirements
    password_validation_results: dict = password_validator.password_validation_result

    # After we are rewriting the user password and print result
    UserDataManipulatorOnLinux.set_user_password(username, new_password)

    print_result_of_set_user_password(username, new_password, password_validation_results)


# Method change existing user password on typed password
def set_typed_password(username: str, typed_password: str) -> None:
    # check password requirements
    password_validator = PasswordValidator(typed_password)
    password_validation_results: dict = password_validator.password_validation_result
    is_password_valid: bool = password_validator.is_password_valid

    if is_password_valid:
        UserDataManipulatorOnLinux.set_user_password(username, typed_password)
        print_result_of_set_user_password(username, typed_password, password_validation_results)
    else:
        print(Fore.RED + '\nYour password is not strong enough' + Style.RESET_ALL)
        print_password_validation_results(password_validation_results)
        change_linux_user_password(username)


# Method ask the user to type a username
# It needs to exist Linux user
def ask_username() -> str:
    entered_username: str = input('Enter a username: ')

    if UserDataManipulatorOnLinux.check_if_user_exists(entered_username):
        return entered_username
    else:
        ask_username()


# Method ask the user to type the new password
def ask_user_to_type_password() -> str:
    return getpass.getpass('Enter a password or press Enter to generate a new one: ')


# Method ask the user to type the password length
# It needs to be at least 8 characters
def ask_password_length() -> int:
    password_length: int = int(input('Please enter the desired password length: '))

    if password_length < 8:
        while password_length < 8:
            print('Your password length must be at least 8 characters!')
            password_length = int(input('Please enter the desired password length: '))

    return password_length


def print_result_of_set_user_password(username: str, password: str, password_validation_results: Dict) -> None:
    print(f'\nUsername: {username}'
          f'\nPassword: {password}')

    if password_validation_results:
        print_password_validation_results(password_validation_results)


def print_password_validation_results(password_validation_results: Dict) -> None:
    for index, password_validation_result in enumerate(password_validation_results):
        print(f"\t{index + 1}. {password_validation_result.replace('_', ' ').title()}: "
              f'{Fore.GREEN if password_validation_results[password_validation_result] else Fore.RED}'
              f"{'✓' if password_validation_results[password_validation_result] else 'X'}" + Style.RESET_ALL)


if __name__ == '__main__':
    linux_username: str = ask_username()

    change_linux_user_password(linux_username)
