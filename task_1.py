import sys

def total_salary(path):
    total = 0
    average = 0
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            lines = [el.strip() for el in fh.readlines()]
            if lines:
                for line in lines:               
                    total += int((line.split(','))[1])
                    average = int(total / len(lines))
                return(total,average)
            print(f"Calculating error: {path} file is empty")
            return sys.exit()
    except Exception as e:
        print(f"File accessing error: {e}")
        return sys.exit()

total, average = total_salary("./salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
