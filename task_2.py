import sys

def get_cats_info(path):
    list = []
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            #Create 'lines' list adding each line from 'path' file, cutting spaces from both sides of each line
            lines = [el.strip() for el in fh.readlines()]
            if lines:
                for line in lines:               
                    #Create list with dictionary elements adding from lines list using ',' separator
                    list.append({"id":((line.split(','))[0]),"name":(line.split(','))[1],"age":(line.split(','))[2]})
                return(list)
            #Error message in case if file is empty
            print(f"Calculating error: {path} file is empty")
            return sys.exit()
    #Handling cases when a file is missing or damaged
    except Exception as e:
        print(f"File accessing error: {e}")
        return sys.exit()

cats_info = get_cats_info("./cats_file.txt")
print(cats_info)
