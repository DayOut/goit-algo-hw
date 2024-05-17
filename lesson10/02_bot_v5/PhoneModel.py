from FieldModel import Field
from exception.PhoneValidationException import PhoneValidationException


class Phone(Field):
    def __init__(self, value: str):
        if len(value) != 10:
            raise PhoneValidationException('Phone number must contain 10 digits')
        super().__init__(value)
