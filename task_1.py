import sys

def total_salary(path):
    total = 0
    average = 0
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            #Create 'lines' list adding each line from 'path' file, cutting spaces from both sides of each line
            lines = [el.strip() for el in fh.readlines()]
            if lines:
                for line in lines:               
                    #Spliting each element from lines list using ',' separator and count sum of each second item from splited elements
                    total += int((line.split(','))[1])
                    #Counting average salary value by dividing total value on record quantity in lines list
                    average = int(total / len(lines))
                return(total,average)
            #Error message in case if file is empty
            print(f"Calculating error: {path} file is empty")
            return sys.exit()
    #Handling cases when a file is missing or damaged
    except Exception as e:
        print(f"File accessing error: {e}")
        return sys.exit()

total, average = total_salary("./salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
