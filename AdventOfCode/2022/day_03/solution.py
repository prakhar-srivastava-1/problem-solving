# create dict of priorities
keys = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
values = range(1, 53)
priorities = dict(zip(keys, values))

# get the input
with open("input.txt", "r") as input_file:
    data = input_file.read()
    data = data.split("\n")

# capture common elements
def get_common_elements(rucksack):
    """
        this method takes in the rucksack, divides it
        into two equal halves and identifies the common
        elements in both halves using set intersection.
        input: str
        returns: list
    """
    # split at the mid
    mid = len(rucksack) // 2
    compartment_1 = set(list(rucksack[0: mid]))
    compartment_2 = set(list(rucksack[mid: ]))
    # print(compartment_1, compartment_2)
    common_elements = compartment_1.intersection(compartment_2)
    return list(common_elements)

def get_priorities(common_elements):
    """
        this method takes in the list of common elements
        and looks up their respective priorities and sums
        them up.
        input: list
        returns: int
    """
    priority_list = [priorities[each] for each in common_elements]
    return sum(priority_list)

# for each rucksack in input
total_priority = 0
for each_rucksack in data:
    common_elements = get_common_elements(each_rucksack.strip())
    total_priority += get_priorities(common_elements)

# total priority
print(total_priority)

# PART TWO
badge_priority = 0
# take three rows at a time
for index in range(0, len(data), 3):
    elf_1 = set(list(data[index].strip()))
    elf_2 = set(list(data[index+1].strip()))
    elf_3 = set(list(data[index+2].strip()))
    
    # get the intersection
    badge = list(elf_3.intersection(elf_1.intersection(elf_2)))
    # get and add the priority
    badge_priority += priorities[badge[0]]

print(badge_priority)