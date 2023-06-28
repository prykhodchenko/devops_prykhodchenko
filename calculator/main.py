from typing import List, Dict

operations_list: List[str] = ['Addition', 'Subtraction', 'Multiplication', 'Division'];


def run_calculator() -> None:
  numbers: Dict[str, float] = prompt_numbers_from_user()
  operation_index: int = prompt_operation_index_from_user()
  result: float = calculate_result(numbers, operations_list[operation_index])

  print('The result of', operations_list[operation_index].lower(), 'is:', result)


def prompt_numbers_from_user() -> Dict[str, float]:
  first_number: float = float(input('Please enter the first number:'))
  second_number: float = float(input('Please enter the second number:'))

  return {'first_number': first_number, 'second_number': second_number}


def prompt_operation_index_from_user() -> int:
  print('Please select an operation:')
  print_operations_list()
  operation_index: int = 0

  while 1 > operation_index or operation_index > 4:
    operation_index: int = int(input('Enter your choice (1-4):'))

  return operation_index - 1


def print_operations_list() -> None:
  for index, operation in enumerate(operations_list, 1):
    print(index, operation, sep='. ')


def calculate_result(numbers: Dict[str, float], operation: str) -> float:
  if operation == operations_list[0]:
    return numbers['first_number'] + numbers['second_number']
  if operation == operations_list[1]:
    return numbers['first_number'] - numbers['second_number']
  if operation == operations_list[2]:
    return numbers['first_number'] * numbers['second_number']
  if operation == operations_list[3]:
    return numbers['first_number'] / numbers['second_number']


if __name__ == '__main__':
  run_calculator()
