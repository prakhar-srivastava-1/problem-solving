# method to print dict - for debugging
def print_dict(all_items):
    for key, value in all_items.items():
        print(f"{key}: {value}")

# read the input file
with open("input.txt", "r") as input_file:
    data = input_file.read()
    data = data.split("\n")

# stores {dir: [files, dirs]}
all_items = {}
# tracks current dir
stack = []

# parse line by line
# get all cd commands
for each_line in data:
    each_line = each_line.split()
    
    if each_line[0] == "$":
        # change directory
        if each_line[1] == "cd":
            # its a cd command
            dir = each_line[2]
            
            if dir == "..":
                stack.pop()
            else:
                stack.append(dir)       

            # create the key - current absolute path
            dir_key = '/'.join(stack)
            dir_key = dir_key.replace("//", "/")
            # add to dict with [] as value
            all_items[dir_key] = all_items.get(dir_key, [])

# holds the ordered list of contents 
# to be later assigned to dir dict
content_list = []

for index in range(len(data)):
    each_line = data[index]
    each_line = each_line.split()
    
    # list
    if each_line[1] == "ls":
        # its a list command
        index += 1
        # holds the contents of a dir
        contents = []
        while not data[index].startswith("$"):
            this_item = data[index].split()
            if this_item[0] == "dir":
                contents.append(this_item[1])
            # case of files - append size
            else:
                contents.append(this_item[0])
            index += 1
            
            if index == len(data):
                break

        content_list.append(contents)  


def get_sum(key, nums_list):
    """
        method to sum up the int sizes and append
        alphabetical dirs to a list and return it
        input: str (current_dir key)
               nums_list (dir contents)
        returns: list
    """
    sum = 0
    dirs = []
    for each in nums_list:
        try:
            sum += int(each)
        except:
            if key != "/":
                dirs.append(f"{key}/{each}")
            else:
                dirs.append(f"/{each}")  
    return [sum] + dirs

ctr = 0
# map dirs to their respective contents
for key in all_items.keys():
    all_items[key] = get_sum(key, content_list[ctr])
    ctr += 1

# list to track which dirs have only numbers (total size)
done = []
while len(done) != len(all_items.keys()):
    for key, value in all_items.items():
        # if there is only one element in list => only size;
        # all child dirs have been replaced with size
        if len(value) == 1 and key not in done:
            done.append(key)

        # replace dir with its size using dicr we created
        for index, each_size in enumerate(value):
            if each_size in done:
                value[index] = all_items[each_size][0]
        
        # sum if all are int; else continue to next iteration
        try:
            all_items[key] = [sum(value)]
        except:
            continue

total_size = 0
for key, value in all_items.items():
    size = value[0]
    if size > 0 and size <= 100000:
       total_size += size

print(total_size)

# PART TWO

MAX_STORAGE = 70000000
NEEDED_FREE_STORAGE = 30000000

total_size_used = all_items["/"][0]
storage_free = MAX_STORAGE - total_size_used
additional_requirement = NEEDED_FREE_STORAGE - storage_free

min_size = MAX_STORAGE

# find dir with minimum size just enough to reach NEEDED_FREE_STORAGE 
for key, value in all_items.items():
    size = value[0]
    if size >= additional_requirement and size < min_size:
        min_size = size

print(min_size)
        