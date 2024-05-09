import os

def total_salary(path: str) -> (int):
    if not os.path.exists(path):
        print("[ERROR] Can't find file in this directory")
        return ()
    
    with open(path) as f:
        line = f.readline()
        sum_salary = 0
        employee_count = 0

        while line:
            items = line.split(',') 
            if len(items) != 2:
                print("[ERROR] Broken row! Can't find salary. Raw line: '" + line.strip() + "'")
                line = f.readline()
                continue

            sum_salary += int(items[-1])
            employee_count += 1
            line = f.readline()
            
        
        avg_salary = round(sum_salary / employee_count, 2)
        return (sum_salary, avg_salary)

salary = total_salary("file.txt")
print('Total salary: ' + str(salary[0]))
print('Average salary: ' + str(salary[1]))