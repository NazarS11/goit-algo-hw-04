import sys

def get_cats_info(path):
    list = []
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            lines = [el.strip() for el in fh.readlines()]
            if lines:
                for line in lines:               
                    list.append({"id":((line.split(','))[0]),"name":(line.split(','))[1],"age":(line.split(','))[2]})
                return(list)
            print(f"Calculating error: {path} file is empty")
            return sys.exit()
    except Exception as e:
        print(f"File accessing error: {e}")
        return sys.exit()

cats_info = get_cats_info("./cats_file.txt")
print(cats_info)
