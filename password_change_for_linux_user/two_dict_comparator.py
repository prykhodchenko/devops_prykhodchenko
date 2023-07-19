#!/usr/bin/env python3

from colorama import Fore, Style


class TwoDictComparator:
    _dict_1: dict = {}
    _dict_2: dict = {}

    def __int__(self, dict_1, dict_2):
        self._dict_1 = dict_1
        self._dict_2 = dict_1

    @property
    def _dict_1(self):
        return self._dict_1

    @property
    def _dict_2(self):
        return self._dict_2

    @_dict_1.setter
    def _dict_1(self, dict_1):
        if not type(dict_1) is dict:
            print(Fore.RED + 'Wrong data type, parameter needs to be a dictionary' + Style.RESET_ALL)
        else:
            self._dict_1 = dict_1

    @_dict_2.setter
    def _dict_2(self, dict_2):
        if not type(dict_2) is dict:
            print(Fore.RED + 'Wrong data type, parameter needs to be a dictionary' + Style.RESET_ALL)
        else:
            self._dict_1 = dict_2

    @staticmethod
    def is_two_dicts_have_the_same_keys(self) -> bool:
        diff = set(self._dict_1.keys()).difference(self._dict_2.keys())

        if not type(diff) is dict:
            return False
        else:
            return True
