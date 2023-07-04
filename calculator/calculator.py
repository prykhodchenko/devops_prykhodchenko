from typing import List, Dict

calculator_operations_list: List[str] = ['Addition', 'Subtraction', 'Multiplication', 'Division'];


def run_calculator() -> None:
  numbers: Dict[str, float] = ask_numbers_from_user()
  operation_index: int = ask_operation_index_from_user()
  result: float = calculate_result(numbers, calculator_operations_list[operation_index])

  print('The result of', calculator_operations_list[operation_index].lower(), 'is:', result)

#Ask user print values for calculation
def ask_numbers_from_user() -> Dict[str, float]:
  first_number: float = get_input_value('Please enter the first number:')
  second_number: float = get_input_value('Please enter the second number:')

  return {'first_number': first_number, 'second_number': second_number}

#Ask user choose operation type
def ask_operation_index_from_user() -> int:
  print('Please select an operation:')
  print_operations_list()

  operation_index: int = 0

  while 1 > operation_index or operation_index > 4:
    operation_index: int = int(input('Enter your choice (1-4):'))

  return operation_index - 1

#Display in console list of operations
def print_operations_list() -> None:
  for index, operation in enumerate(calculator_operations_list, 1):
    print(index, operation, sep='. ')


#Return result of calculation
def calculate_result(numbers: Dict[str, float], operation: str) -> float or str:
  if operation == calculator_operations_list[0]:
    return numbers['first_number'] + numbers['second_number']
  if operation == calculator_operations_list[1]:
    return numbers['first_number'] - numbers['second_number']
  if operation == calculator_operations_list[2]:
    return numbers['first_number'] * numbers['second_number']
  if operation == calculator_operations_list[3]:
    try:
      return numbers['first_number'] / numbers['second_number']
    except ZeroDivisionError:
      return 'Cannot divide by zero'
def get_input_value (message: str):
  while True:
    try:
      num = float(input(message))
    except ValueError:
      print('Please enter an integer or float')
      continue
    if isinstance(num, float):
      return num




if __name__ == '__main__':
  run_calculator()
