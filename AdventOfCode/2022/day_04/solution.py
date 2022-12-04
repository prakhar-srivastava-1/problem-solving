# read the input
with open("input.txt", "r") as input_file:
    data = input_file.read()
    data = data.split("\n")

"""
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

def have_commons(elf_1, elf_2):
    """
        finds out the fully contained sets
        inputs: list, list
        returns: bool
    """
    # if elf_1 list contains elf_2 list
    if elf_1[0] <= elf_2[0] and elf_1[1] >= elf_2[1]:
        return True
    
    # if elf_2 list contains elf_1 list
    if elf_2[0] <= elf_1[0] and elf_2[1] >= elf_1[1]:
        return True
    
    # default
    return False

pairs = 0
for each_line in data:
    # assign the sections to elves
    each_line = each_line.strip()
    elves = each_line.split(",")
    elf_1, elf_2 = elves[0], elves[1]
    
    # get numbers for elf_1 
    elf_1 = elf_1.split("-")
    elf_1 = [int(elf_1[0]), int(elf_1[1])]

    # get numbers for elf_2 
    elf_2 = elf_2.split("-")
    elf_2 = [int(elf_2[0]), int(elf_2[1])]

    if have_commons(elf_1, elf_2):
        pairs += 1

print(pairs)

# PART TWO

def have_any_commons(elf_1, elf_2):
    """
        finds if there is even a single overlap
        inputs: list, list
        returns: bool
    """
    # if elf_1 list contains anything from elf_2 list
    if elf_1[0] <= elf_2[0] and elf_1[1] >= elf_2[0] \
       or elf_1[0] <= elf_2[1] and elf_1[1] >= elf_2[1]:
        return True
    
    # if elf_2 list contains anything from elf_1 list
    if elf_2[0] <= elf_1[0] and elf_2[1] >= elf_1[0] \
       or elf_2[0] <= elf_1[1] and elf_2[1] >= elf_1[1]:
        return True
    
    # default
    return False 


pairs_2 = 0
for each_line in data:
    # assign the sections to elves
    each_line = each_line.strip()
    elves = each_line.split(",")
    elf_1, elf_2 = elves[0], elves[1]
    
    # get numbers for elf_1 
    elf_1 = elf_1.split("-")
    elf_1 = [int(elf_1[0]), int(elf_1[1])]

    # get numbers for elf_2 
    elf_2 = elf_2.split("-")
    elf_2 = [int(elf_2[0]), int(elf_2[1])]

    if have_any_commons(elf_1, elf_2):
        pairs_2 += 1

print(pairs_2)