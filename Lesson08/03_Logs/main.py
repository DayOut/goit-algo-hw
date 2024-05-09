import os, re
import json
from colorama import Fore, Back, init

from sys import argv
from collections import defaultdict


LOG_PATTERN = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(INFO|DEBUG|ERROR|WARNING)\s+(.*)"

ERROR_FORE_COLOR = Fore.RED
ERROR_BACK_COLOR = Back.RED

def parse_log_line(line: str) -> dict:
    line = line.strip()
    match = re.match(LOG_PATTERN, line)
    if not match:
        print(f"[WARNING] Row has incomplete data: '{line}'")
        return {}
        
    date = match.group(1)
    level = str(match.group(2)).upper()
    message = match.group(3)
    return {"date": date, "level": level, "message": message}

def load_logs(file_path: str) -> list:
    # мені здається, що у випадку завантаження великого файлу ми впремось в памʼять компютера. 
    # Тож не варто завантажувати все в памʼять. Але ТЗ є ТЗ ¯\_(ツ)_/¯
    if not os.path.exists(file_path):
        print(print_error("Can't find file in this directory"))
        return []
    
    result = []
    with open(file_path) as file:
        line = file.readline()
        while line:
            parsedLine = parse_log_line(line)
            if parsedLine == {}:
                line = file.readline()
                continue
            result.append(parsedLine)
            line = file.readline()
    return result

def filter_logs_by_level(logs: list, level: str) -> list:
    log_filter = filter(lambda log: log['level'] == level, logs)
    filteredLogs = list(log_filter)
    if len(filteredLogs) == 0:
        print(print_warning(f"There is no records for level '{level}'")) 
        return
    
    print("\n" + print_info(f"Деталі логів для рівня '{level}':"))
    for record in filteredLogs:
        print(f"{record['date']} - {record['message']}")


def count_logs_by_level(logs: list) -> dict:
    result = defaultdict(int)
    for record in logs:
        result[record['level']] += 1
    
    sortedResult = dict(sorted(result.items()))
    return sortedResult

def display_log_counts(counts: dict):
    print(print_info(f'{'Рівень логування':<20}| {'Кількість':<10}'))
    for key, item in counts.items():
        print(f'{Fore.BLUE}{key:<20}| {item:<10}')
    print()

def print_error(msg: str):
    return f"{ERROR_BACK_COLOR}{'[Error]':^7}{Back.RESET}{ERROR_FORE_COLOR} {msg}"

def print_warning(msg: str):
    return f"{Back.YELLOW}{'[Warning]':^7}{Back.RESET}{Fore.YELLOW} {msg}"

def print_info(msg: str):
    return f"{Back.BLUE}{msg}"


def main():
    try:
        init(autoreset=True)
        if len(argv) < 2:
            print(print_error("Argument was not found! Expected path to log file"))
            return

        filePath = argv[1]

        logs = load_logs(filePath)
        if len(logs) == 0:
            return
        
        display_log_counts(count_logs_by_level(logs))

        if len(argv) > 2:
            errLevel = str(argv[2]).upper()
            filter_logs_by_level(logs, errLevel)
    except Exception as error:
        print(print_error("Unexpected error:"), error)

if __name__ == "__main__":
    main()