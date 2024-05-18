from .NameModel import Name
from .BirthdayModel import Birthday
from .PhoneModel import Phone

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)

    def show_birthday(self):
        if not self.birthday:
            raise Exception("Birthday was not defined. Please add date to this contact")
        return str(self.birthday)
    
    def has_birthday(self):
        return type(self.birthday) == Birthday

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

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
    
    def all_phones(self):
        return ''.join(f"{p.value:>15};" for p in self.phones)

    # def __str__(self):
    #     return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"