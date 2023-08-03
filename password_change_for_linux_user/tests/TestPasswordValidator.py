import unittest

from password_change_for_linux_user.password_validator import PasswordValidator


class PasswordValidatorTestCase(unittest.TestCase):
    __correct_password = '123456aA1'
    __password_without_digit = 'asdfasd@@@SS'
    __password_without_punctuation = 'asdfasd12WSSs'
    __password_without_lower_case_letter = '123!!@DDDDDDD'
    __password_without_upper_case_letter = '123!!@rrrrwqwe'
    __password_with_wrong_length = '12!!@rD'
    __password_validation_requirements = ['password_length', 'punctuation', 'upper_case_char',
                                          'lower_case_char', 'digit']

    def setUp(self) -> None:
        self.password_validator = PasswordValidator()

    def test_if_correct_password_is_valid(self) -> None:
        self.password_validator.validate_password(self.__correct_password)
        self.assertTrue(self.password_validator.is_password_valid, 'Error: Password is not valid'
                                                                   'Expectation: Password is valid')

    def test_if_password_without_digit_is_not_valid(self) -> None:
        self.password_validator.validate_password(self.__password_without_digit)
        self.assertFalse(self.password_validator.is_password_valid, 'Error: Password is valid'
                                                                    'Expectation: Password is not valid')

    def test_if_password_without_punctuation_is_not_valid(self) -> None:
        self.password_validator.validate_password(self.__password_without_punctuation)
        self.assertFalse(self.password_validator.is_password_valid, 'Error: Password is valid'
                                                                    'Expectation: Password is not valid')

    def test_if_password_without_lower_case_letter_is_not_valid(self) -> None:
        self.password_validator.validate_password(self.__password_without_lower_case_letter)
        self.assertFalse(self.password_validator.is_password_valid, 'Error: Password is valid'
                                                                    'Expectation: Password is not valid')

    def test_if_password_without_upper_case_letter_is_not_valid(self) -> None:
        self.password_validator.validate_password(self.__password_without_lower_case_letter)
        self.assertFalse(self.password_validator.is_password_valid, 'Error: Password is valid'
                                                                    'Expectation: Password is not valid')

    def test_if_password_with_wrong_length_is_not_valid(self) -> None:
        self.password_validator.validate_password(self.__password_with_wrong_length)
        self.assertFalse(self.password_validator.is_password_valid, 'Error: Password is valid'
                                                                    'Expectation: Password is not valid')

    def test_if_all_validation_requirements_has_applied(self) -> None:
        applied_password_validator_requirements = self.password_validator.password_validation_result.keys()
        self.assertTrue(applied_password_validator_requirements == self.__password_validation_requirements,
                        f'Not all requirements has applied!'
                        f"Applied requirements: {', '.join(applied_password_validator_requirements)}"
                        f"Expectation: {', '.join(self.__password_validation_requirements)}")


if __name__ == '__main__':
    unittest.main()
