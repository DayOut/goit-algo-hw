import os
import pickle

from colorama import Fore, Back, Style, init
from collections import UserDict
from Models.AddressBookModel import AddressBook
from Models.RecordModel import Record

BOT_FORE_COLOR = Fore.CYAN
BOT_BACK_COLOR = Back.CYAN
USER_FORE_COLOR = Fore.BLACK
USER_BACK_COLOR = Back.LIGHTBLACK_EX
ERROR_FORE_COLOR = Fore.RED
ERROR_BACK_COLOR = Back.RED

is_last_command = False


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return f"{ERROR_FORE_COLOR}Can't find record with this arguments"
        except IndexError:
            return f"{ERROR_FORE_COLOR}Can't find record with this arguments"
        except ValueError:
            return f"{ERROR_FORE_COLOR}Give me name and phone please"

    return inner


def not_found_error(func):
    def inner(*args, **kwargs):
        arguments, book, *_ = args
        name = arguments[0]
        record = book.find(name)
        if record is None:
            raise Exception(f"Contact with name '{
                            bold_str(name)}' was not found")
        return func(*args, **kwargs)
    return inner


def capitalize_name(func):
    def inner(*args, **kwargs):
        args[0][0] = str(args[0][0]).capitalize()
        return func(*args, **kwargs)
    return inner


@capitalize_name
@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    name = str(name).capitalize()
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@capitalize_name
@not_found_error
@input_error
def change_contact(args, book: AddressBook):
    name, phone_before, phone_after = args
    record = book.find(name)
    record.edit_phone(phone_before, phone_after)
    return 'Contact updated'


@capitalize_name
@not_found_error
@input_error
def show_contact(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    return f"{name}: {record.all_phones()}"


def show_all_contacts(args, book: AddressBook):
    phoneBook = ''
    for name, phone in book.items():
        phoneBook = phoneBook + \
            f"{name.capitalize():^15}: {phone.all_phones()} \n"
    return f"Your phone books: \n{phoneBook}"


@capitalize_name
@not_found_error
@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    record.add_birthday(birthday=birthday)
    return "Birthday was added successfully"


@capitalize_name
@not_found_error
@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    return f"Birthday for {bold_str(name)} is {record.show_birthday()}"


@input_error
def birthdays(args, book: AddressBook):
    birthdays = book.get_upcoming_birthdays()
    if len(birthdays) == 0:
        return "Don't worry, there is no upcoming birthdays ;)"

    message = "There is some records with upcoming birthdays:"
    for greeting in book.get_upcoming_birthdays():
        message = f"{message}\n{bold_str(greeting['name']):>20} at {
            greeting['congratulation_date']}"
    return message


def hello(args, book: AddressBook):
    return "How can I help you?"


def clear_screen(args, book: AddressBook):
    os.system("clear")
    return 'Cleared screen'


def close_app(args=None, book: AddressBook = None):
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
    "all": show_all_contacts,
    "add-birthday": add_birthday,
    "show-birthday": show_birthday,
    "birthdays": birthdays,
}


def main():
    init(autoreset=True)
    os.system("clear")
    book = load_data()

    print(print_bot("Welcome to the assistant bot!"))

    try:
        while True:
            user_input = input(print_user("Enter a command: "))
            command, *args = parse_input(user_input)

            command_function = ALLOWED_COMMANDS.get(command)
            if command_function != None:
                try:
                    print(print_bot(command_function(args, book)))
                except Exception as e:
                    print(print_error(e))

                if is_last_command:
                    break
            else:
                print(print_error(f"Invalid command \"{command}\""))
    except KeyboardInterrupt:
        print()
        print(print_bot("Keyboard interrupt."))
        print(print_bot(close_app()))
    finally:
        save_data(book)


if __name__ == "__main__":
    main()
