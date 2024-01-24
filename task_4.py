from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Визначення днів народження на наступний тиждень
        days_until_birthday = (birthday - today).days
        if 0 <= days_until_birthday <= 7:
            # Переносимо на наступний рік, якщо день народження вже минув цього року
            birthday_this_year = birthday.replace(year=today.year)
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            # Перевірка, чи день народження припадає на вихідний
            if birthday_this_year.weekday() in [5, 6]:
                # Перенесення дати привітання на наступний понеділок
                monday = today + timedelta(days=(7 - today.weekday()) + 1)
                congratulation_date = monday.strftime("%Y.%m.%d")
            else:
                congratulation_date = birthday_this_year.strftime("%Y.%m.%d")

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date
            })

    return upcoming_birthdays

# Приклад використання
users = [
    {"name": "John Doe", "birthday": "2024.01.30"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:")
for birthday_info in upcoming_birthdays:
    print(f"{birthday_info['name']} - {birthday_info['congratulation_date']}")
