from .FieldModel import Field
from datetime import datetime


class Birthday(Field):
    def __init__(self, value):
        self.birthday = None
        try:
            self.birthday = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
    
    def __str__(self):
        return datetime.strftime(self.birthday, "%d.%m.%Y")
