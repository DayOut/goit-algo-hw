import re

def normalize_phone(phone_number: str) -> str:
    # Видаляємо всі нецифрові символи
    number = re.sub(r'\D', '', phone_number)
    
    # Видаляємо префікси '380', '38', а також '0' перед кодом мобільного оператора
    if number.startswith('380'):
        number = number[3:]
    elif number.startswith('38'):
        number = number[2:]
    elif number.startswith('0'):
        number = number[1:]
    
    # Додаємо код мобільного оператора
    if len(number) == 9:
        number = '+380' + number
    
    # Форматуємо номер 
    formatted_number = re.sub(r'(\d{3})(\d{3})(\d{2})(\d{2})', r'\1\2\3\4', number)
    
    # Додаємо нормалізований номер до списку
    return formatted_number
    
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)