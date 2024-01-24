import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр
    cleaned_number = re.sub(r'\D', '', phone_number)

    # Перевіряємо, чи номер починається з '38' або '380'
    if cleaned_number.startswith('38') and len(cleaned_number) > 9:
        # Видаляємо '38' або '380' з початку номера
        cleaned_number = cleaned_number[2:]

    # Додаємо міжнародний код '+38' до номера
    cleaned_number = '+38' + cleaned_number

    return cleaned_number

# Приклад використання
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
    "383812345678"  # Додано випадок з '3838'
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

# Виведення результатів
for original, sanitized in zip(raw_numbers, sanitized_numbers):
    #print(f"Оригінальний номер: {original}")
    print(f"Нормалізований номер: {sanitized}\n")
