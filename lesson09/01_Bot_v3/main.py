from collections import UserDict


class PhoneValidationException(Exception):
    pass


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


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

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


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

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
