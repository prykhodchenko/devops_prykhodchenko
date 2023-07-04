#!/usr/bin/env python3

import getpass
from typing import Dict
from colorama import Fore, Style

from user_data_manipulator_on_linux import UserDataManipulatorOnLinux
from password_generator import PasswordGenerator


# The initial method of password change
def change_linux_user_password(username: str) -> None:
  typed_password: str = ask_user_to_type_password()

  if typed_password:
    set_typed_password(username, typed_password)
  else:
    set_auto_generated_password(username)


# Setting auto-generated password
def set_auto_generated_password(username: str) -> None:
  #ask the user to print the password length.
  password_length: int = PasswordGenerator.ask_password_length()

  # generate a strong password
  new_password: str = PasswordGenerator.generate_password(password_length)

  #check password requirements
  password_requirements_results: Dict = PasswordGenerator.check_password_requirements(new_password)

  # After we are rewriting the user password and print result
  UserDataManipulatorOnLinux.set_user_password(username, new_password)
  print_result_of_set_user_password(username, new_password, password_requirements_results)

# Setting typed password
def set_typed_password(username: str, typed_password: str) -> None:
  #check password requirements
  password_requirements_results: Dict = PasswordGenerator.check_password_requirements(typed_password)

  if all(password_requirements_results.values()):
    UserDataManipulatorOnLinux.set_user_password(username, typed_password)
    print_result_of_set_user_password(username, typed_password, password_requirements_results)
  else:
    print(password_requirements_results)
    print(Fore.RED + '\nYour password is not strong enough' + Style.RESET_ALL)
    print_password_requirements_results(password_requirements_results)
    change_linux_user_password(username)


def ask_username() -> str:
  entered_username: str = input('Enter a username: ')

  if UserDataManipulatorOnLinux.check_if_user_exists(entered_username):
    return entered_username
  else:
    ask_username()


def ask_user_to_type_password() -> str:
  return getpass.getpass('Enter a password or press Enter to generate a new one: ')


def print_result_of_set_user_password(username: str, password: str, password_requirements_results: Dict) -> None:
  print(f'\nUsername: {username}')
  print(f'Password: {password}')

  if password_requirements_results:
    print_password_requirements_results(password_requirements_results)


def print_password_requirements_results(password_requirements_results: Dict) -> None:
  for index, password_requirements_result in enumerate(password_requirements_results):
    print(f"\t{index + 1}. {password_requirements_result.replace('_', ' ').title()}: "
          f'{Fore.GREEN if password_requirements_results[password_requirements_result] else Fore.RED}'
          f"{'✓' if password_requirements_results[password_requirements_result] else 'X'}" + Style.RESET_ALL)


if __name__ == '__main__':
  username: str = ask_username()

  change_linux_user_password(username)
