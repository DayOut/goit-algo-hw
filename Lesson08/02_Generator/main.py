import re
 
def is_float_regex(value):
    return bool(re.match(r'^[-+]?[0-9]*\.?[0-9]+$', value))

def generator_numbers(text: str):
    words = text.split(' ')
    for word in words:
        if is_float_regex(word):
            yield float(word)

def sum_profit(text: str, func: callable):
    profit = 0
    for profitFromText in func(text):
        profit += profitFromText
    return profit

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")