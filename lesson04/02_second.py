import random

def get_numbers_ticket(min: int, max: int, qty: int) -> list[int]:
    if min < 1 or max > 1000:
        return []

    result = []
    while len(result) < qty:
        randomValue = random.randint(min, max)
        if randomValue not in result:
            result.append(randomValue)
        
    result.sort()

    return result

print(f"Ваші лотерейні числа: {get_numbers_ticket(1, 49, 6)}")
