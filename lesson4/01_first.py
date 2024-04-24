from datetime import datetime

def get_days_from_today(dateString: str, nowString: str  = "") -> str:
    try:
        # параметр nowString заданий виключно для тесту
        if ("" != nowString):
            # якщо тестуємо і задали конкретну дату, то конвертуємо строку в дату
            now =  datetime.strptime(nowString, "%Y-%m-%d")
        else:
            # якщо не тестуємо, то беремо реальну поточну дату
            now = datetime.today()

        parsedDate = datetime.strptime(dateString, "%Y-%m-%d")
        delta = parsedDate - now
    except ValueError:
        return "Формат дати не відповідає очікуванному."
    return str(delta.days)

print(f"From today: {get_days_from_today("2021-10-09")}")
print(f"From test:  {get_days_from_today("2021-10-09", "2021-05-05")}")
print(f"Wrong format: {get_days_from_today("2021/10/09")}")
