from colorama import Fore, Back, Style, init
from collections import UserDict
from datetime import datetime

BOT_FORE_COLOR = Fore.CYAN
BOT_BACK_COLOR = Back.CYAN
USER_FORE_COLOR = Fore.BLACK
USER_BACK_COLOR = Back.LIGHTBLACK_EX
ERROR_FORE_COLOR = Fore.RED
ERROR_BACK_COLOR = Back.RED

class PhoneValidationException(Exception):
    pass

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

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def change(self, value):
        self.value = value


class Name(Field):
    # реалізація класу
    pass


class Phone(Field):
    def __init__(self, value: str):
        if len(value) != 10:
            raise PhoneValidationException
        super().__init__(value)
    pass


class Birthday(Field):
    def __init__(self, value):
        self.birthday = None
        try:
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
            self.birthday = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)

    def add_phone(self, phone: str):
        try:
            self.phones.append(Phone(phone))
        except PhoneValidationException:
            print('Something wrong with this number')

    def remove_phone(self, phone: str):
        self.phones = list(
            filter(lambda item: str(item) != phone, self.phones))

    def edit_phone(self, number_before, number_after):
        for number in self.phones:
            if str(number) == number_before:
                number.change(number_after)
                break

    def find_phone(self, target_number):
        for number in self.phones:
            if str(number) == target_number:
                return str(number)
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[str(record.name)] = record

    def find(self, name: str) -> Record:
        for key, record in self.data.items():
            if str(record.name) == name:
                return record
        return None

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]
            print(f"Запис для {name} успішно видалено.")
        return None

    def get_upcoming_birthdays(self,  now: datetime):
        result = []
        for key, record in self.data.items():
            if not record.birthday:
                continue

            userBirthday = record.birthday.birthday
            userBirthday = userBirthday.replace(year=now.year)
            delta = now - userBirthday
            if abs(delta.days) <= 7:
                if userBirthday.weekday() >= 5:
                    correction = 7 - userBirthday.weekday()
                    userBirthday = userBirthday.replace(
                        day=(userBirthday.day + correction))
                result.append(
                    {'name': key, 'congratulation_date': userBirthday.strftime("%Y.%m.%d")})
        for greeting in result:
            print(
                f"Don't forget to say Happy Birthday to {greeting['name']} at {greeting['congratulation_date']}")


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_birthday("12.06.1997")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

today = datetime.strptime("2024.06.10", "%Y.%m.%d")
book.get_upcoming_birthdays(today)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555
john.remove_phone("5555555555")

# Видалення запису Jane
book.delete("Jane")
