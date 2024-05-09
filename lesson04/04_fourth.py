from datetime import datetime

def get_upcoming_birthdays(users: list, now: datetime) -> list:
    result = []
    for user in users:
        userBirthday = datetime.strptime(user['birthday'], "%Y.%m.%d")
        userBirthday = userBirthday.replace(year=now.year)
        delta = now - userBirthday
        if abs(delta.days) <= 7:
            if userBirthday.weekday() >= 5:
                correction = 7 - userBirthday.weekday()
                userBirthday = userBirthday.replace(day=(userBirthday.day + correction))
            result.append({'name': user['name'], 'congratulation_date': userBirthday.strftime("%Y.%m.%d")})
    return result

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane1 Smith", "birthday": "1990.02.27"},
    {"name": "Jane2 Smith", "birthday": "1990.03.27"},
    {"name": "Jane3 Smith", "birthday": "1990.04.27"},
    {"name": "Jane4 Smith", "birthday": "1990.05.27"},
    {"name": "Jane5 Smith", "birthday": "1990.06.27"},
    {"name": "Jane6 Smith", "birthday": "1990.07.27"},
    {"name": "Jane7 Smith", "birthday": "1990.08.27"},
    {"name": "Jane8 Smith", "birthday": "1990.09.27"},
    {"name": "Jan9 Smith", "birthday": "1990.10.27"},
    {"name": "Jane10 Smith", "birthday": "1990.11.27"},
    {"name": "John Doe", "birthday": "1985.01.20"},
]

today = datetime.strptime("2024.01.22", "%Y.%m.%d")

upcoming_birthdays = get_upcoming_birthdays(users, today)
print("Список привітань на цьому тижні:", upcoming_birthdays)
