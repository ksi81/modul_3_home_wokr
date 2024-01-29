from datetime import datetime as dt


def get_days_from_today():
  try:
    # Введення користувача дати у форматі 'РРРР-ММ-ДД'
    user_input = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")

    # Перетворення рядка дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
    input_date = dt.strptime(user_input, '%Y-%m-%d')
    #input_date = dt(2021, 5, 5)
    # Отримання поточної дати
    current_date = dt.today()
    #current_date = dt(2021, 10, 9)

    # Розрахунок різниці між поточною датою та введеною користувачем датою
    difference = current_date - input_date

    # Повернення різниці у днях як ціле число
    return difference.days
  except ValueError:
    # Обробка винятків для неправильного формату вхідних даних
    return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."


# Приклад виклику функції
result = get_days_from_today()

print(f"Різниця у днях: {result}")
#test
