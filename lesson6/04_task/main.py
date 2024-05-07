import os
from colorama import Fore, Back, Style, init

BOT_FORE_COLOR = Fore.CYAN
BOT_BACK_COLOR = Back.CYAN
USER_FORE_COLOR = Fore.BLACK
USER_BACK_COLOR = Back.LIGHTBLACK_EX
ERROR_FORE_COLOR = Fore.RED
ERROR_BACK_COLOR = Back.RED

is_last_command = False
contacts = {
    "asd": 123123123,
    "andrew": 321321231,
}

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args) -> bool:
    name, phone = args
    contacts[name] = phone
    return 'Contact added'
    

def change_contact(args) -> bool:
    name = args[0]
    if contacts.get(name) == None:
        return f"{ERROR_FORE_COLOR}Contact with name '{bold_str(name)}' was not found"
    name, phone = args
    contacts[name] = phone
    return 'Contact updated'
    

def show_contact(args) -> bool:
    name = args[0]
    if contacts.get(name):
        return f"{name}: {contacts[name]}"
    else:
        return f"{ERROR_FORE_COLOR}Contact with name '{bold_str(name)}' was not found"
    
def show_all_contacts():
    phoneBook = ''
    for name, phone in contacts.items():
        phoneBook = phoneBook + f"{name.capitalize():^15}: {phone} \n"
    return f"Your phone books: \n{phoneBook}"

def hello(): 
    return "How can I help you?"

def clear_screen():
    os.system("clear")
    return 'Cleared screen'

def close_app(): 
    global is_last_command
    is_last_command = True
    return "Good bye!"

def print_error(msg: str):
    return f"{ERROR_BACK_COLOR}{'[Error]':^7}{Back.RESET}{ERROR_FORE_COLOR} {msg}"

def print_bot(msg: str):
    return f"{BOT_BACK_COLOR}{'[Bot]':^7}{Back.RESET}{BOT_FORE_COLOR} {msg}"

def print_user(msg: str):
    return f"{USER_BACK_COLOR}{'[You]':^7}{Back.RESET}{USER_FORE_COLOR} {msg}"

def bold_str(msg):
    return f"{Style.BRIGHT}{msg}{Style.NORMAL}"

ALLOWED_COMMANDS = {
    "close": close_app,
    "exit": close_app,
    "clear": clear_screen,
    "hello": hello,
    "add": add_contact,
    "change": change_contact,
    "phone": show_contact,
    "all": show_all_contacts
}

def main():
    init(autoreset=True)
    os.system("clear")

    print(print_bot("Welcome to the assistant bot!"))

    try:
        while True:
            user_input = input(print_user("Enter a command: "))
            command, *args = parse_input(user_input)

            command_function = ALLOWED_COMMANDS.get(command)
            if command_function != None:
                try:

                    if not args:
                        print(print_bot(command_function()))
                    else:
                        print(print_bot(command_function(args)))
                    
                    if is_last_command:
                        break
                except TypeError:
                    print(print_error(f"Missed some parameters"))
            else:
                print(print_error(f"Invalid command \"{command}\""))
    except KeyboardInterrupt:
        print()
        print(print_bot("Keyboard interrupt."))
        print(print_bot(close_app()))

if __name__ == "__main__":
    main()
