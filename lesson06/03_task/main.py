import os
from colorama import Fore, Back, init

from sys import argv

DIRECTORY_COLOR = Fore.BLUE
FILE_COLOR = Fore.GREEN
DISPLAY_INDENT = "  "
SHOW_DEV_FOLDERS = '-f'

def print_error(message: str) -> None:
    print(Back.RED + "[ERROR]" + Back.RESET + Fore.RED + " " + message)

def print_info(message: str) -> None:
    print(Back.LIGHTBLACK_EX + "[INFO]" + Back.RESET + Fore.LIGHTBLACK_EX + " " + message)

def show_path_pretty(path: str, indent: str = '', is_dev: bool = False) -> None:
    for item in os.listdir(path):
        element = f"{path}/{item}"
        if os.path.isdir(element): 
            if item[0] == '.' and not is_dev:
                print(indent + DIRECTORY_COLOR + item + "/" 
                      + Fore.YELLOW + "[Dev folder. Skipping]" )
                continue
            else:
                print(indent + DIRECTORY_COLOR + item + "/")
            show_path_pretty(element, indent + DISPLAY_INDENT, is_dev=is_dev)
        else:
            print(indent + FILE_COLOR + item)

        
init(autoreset=True)
if len(argv) == 0:
    print_error("Argument was not found! Expected path to directory")
    
is_dev_flag = False
if len(argv) == 3:
    if argv[2] != SHOW_DEV_FOLDERS:
        print_error("Unknown arguments. Expected path and '-f' for displaying dev folders")
    else:
        print_info("Displaying all directories and files")
        is_dev_flag = True
else:
    print_info("Dev foldes will be hidden. If you want to display all files and folders, you can add flag '-f'")


path = argv[1]
if not os.path.exists(path):
    print_error(f"Can't find directory by path: {path}")

show_path_pretty(path, is_dev=is_dev_flag)
    
