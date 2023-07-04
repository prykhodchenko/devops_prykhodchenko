#!/usr/bin/env python3

import string
import random
import numpy as np
from typing import List


# define the characters
uppercase_letters: str = string.ascii_uppercase
lowercase_letters: str = string.ascii_lowercase
digits: str = string.digits
ascii_characters: str = string.punctuation
all_characters: str = digits + lowercase_letters + ascii_characters + uppercase_letters

def generate_password() -> None:
  print('Welcome to the Linux User Password Generator!')

  password_length: int = ask_password_length()
  required_characters: List[str] = get_required_characters()
  password_length_without_required_characters: int = password_length - len(required_characters)
  random_chose_characters: List[str] = random.choices(all_characters, weights = None, k = password_length_without_required_characters)
  password_list: List[str] = np.concatenate((random_chose_characters, required_characters))

  random.shuffle(password_list)

  password: str = list_to_string(password_list)

  print('Generated password: ', password)


#Ask use to type password length
# need be at least 8characters

def  ask_password_length() -> int:
  while True:
    try:
      password_length = int(input('Please enter the desired password length: '))
    # Handle errors when int input is empty or not an int
    except ValueError:
      print('Please enter an integer')
      continue
    if password_length > 8:
      return password_length
    else:
      # Handle errors when password_length less than 8
      print('Your password length must be at least 8 characters!')

#Ruturn random required characters
def get_required_characters() -> List[str]:
  return [
    random.choices(uppercase_letters, weights=None, k=1)[0],
    random.choices(lowercase_letters, weights=None, k=1)[0],
    random.choices(ascii_characters, weights=None, k=1)[0],
    random.choices(digits, weights=None, k=1)[0],
  ]

def list_to_string(list) -> str:
  str = ''

  for list_el in list:
    str += list_el

  return str

if __name__ == '__main__':
  generate_password()
