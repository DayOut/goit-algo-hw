class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def change(self, value):
        self.value = value