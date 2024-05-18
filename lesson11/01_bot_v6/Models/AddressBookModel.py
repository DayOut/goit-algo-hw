from collections import UserDict
# from NameModel import Name
# from BirthdayModel import Birthday
# from PhoneModel import Phone
from .RecordModel import Record
from datetime import datetime
# from exception.PhoneValidationException import PhoneValidationException


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

    def get_upcoming_birthdays(self):
        now = datetime.now()
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
        return result