#!/usr/bin/env python3

import subprocess
from typing import List

from colorama import Fore, Style


class UserDataManipulatorOnLinux:
    @staticmethod
    def check_if_user_exists(username: str) -> bool:
        # run id command in Linux to find out the user
        try:
            subprocess.check_output(['id', username])
            print(Fore.GREEN + f'User {username} exists in the system!' + Style.RESET_ALL)
            return True
        except subprocess.CalledProcessError as error:
            print(Fore.RED + f'Error: {error}' + Style.RESET_ALL)
            return False

    @staticmethod
    def set_user_password(username: str, password: str) -> None:
        try:
            # Generate the command to change the user password
            command: List[str] = ['dscl', '.', '-passwd', '/Users/' + username, password]

            # Execute the command using subprocess and change user password
            subprocess.run(command, check=True)
            print(Fore.GREEN + 'Password changed successfully!' + Style.RESET_ALL)
        except subprocess.CalledProcessError as error:
            print(Fore.RED + f'Error: {error}' + Style.RESET_ALL)
