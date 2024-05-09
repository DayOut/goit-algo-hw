import os
import re

ROW_PATTERN = r'(\w+),(\w+),(\d+)'

def get_cats_info(path: str) -> list:
    print(os.listdir())
    if not os.path.exists(path):
        print("[ERROR] Can't find file in this directory")
        return []
    result = []
    with open(path) as file:
        line = file.readline()
        while line:
            line = line.strip()
            if not re.match(ROW_PATTERN, line):
                print(f"[WARNING] Row has incomplete data: '{line}'")
                line = file.readline()
                continue
            id, name, age = line.split(',')
            result.append({"id": id, "name": name, "age": age})
            line = file.readline()
    return result


cats_info = get_cats_info("file.txt")
print(cats_info)