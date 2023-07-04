#!/usr/bin/env python3

import string
import random
import numpy as np
from typing import List, Dict


class PasswordGenerator:
  uppercase_letters: str = string.ascii_uppercase
  lowercase_letters: str = string.ascii_lowercase
  digits: str = string.digits
  ascii_characters: str = string.punctuation
  all_characters: str = digits + lowercase_letters + ascii_characters + uppercase_letters

  @staticmethod
  def check_password_requirements(password: str) -> Dict:
    password_requirements_results: Dict = {
      'password_length': len(password) >= 8,
      'punctuation': False,
      'upper_case_char': False,
      'lower_case_char': False,
      'digit': False
    }

    for i in password:
      if i in string.punctuation:
        password_requirements_results['punctuation'] = True
      elif i.isupper():
        password_requirements_results['upper_case_char'] = True
      elif i.islower():
        password_requirements_results['lower_case_char'] = True
      elif i.isdigit():
        password_requirements_results['digit'] = True

    return password_requirements_results

  @staticmethod
  def ask_password_length() -> int:
    password_length: int = int(input('Please enter the desired password length: '))

    if password_length < 8:
      while password_length < 8:
        print('Your password length must be at least 8 characters!')
        password_length = int(input('Please enter the desired password length: '))

    return password_length

  @classmethod
  def generate_password(cls, password_length: int) -> str:
    required_characters: List[str] = PasswordGenerator.get_required_characters()
    password_length_without_required_characters: int = password_length - len(required_characters)
    random_chose_characters: List[str] = random.choices(cls.all_characters, weights=None,
                                                        k=password_length_without_required_characters)
    password_list: List[str] = np.concatenate((random_chose_characters, required_characters))

    random.shuffle(password_list)

    return PasswordGenerator.list_to_string(password_list)

  @staticmethod
  def list_to_string(list: List[str]) -> str:
    string: str = ''

    for list_el in list:
      string += list_el

    return string

  @classmethod
  def get_required_characters(cls) -> List[str]:
    return [
      random.choices(cls.uppercase_letters, weights=None, k=1)[0],
      random.choices(cls.lowercase_letters, weights=None, k=1)[0],
      random.choices(cls.ascii_characters, weights=None, k=1)[0],
      random.choices(cls.digits, weights=None, k=1)[0],
    ]
