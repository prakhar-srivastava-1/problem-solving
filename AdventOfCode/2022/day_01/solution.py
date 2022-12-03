# read input data
with open("input.txt", "r") as input_file:
    data = input_file.read()
    data = data.split("\n")

# save sums of each elf's bag
sum_of_calories = []
# saves one elf's bag at a time
calories = []
for line in data:
    # move to next elf if a blank is encountered
    if line == "":
        # append the sum to main list
        sum_of_calories.append(sum(calories))
        # empty the bag for next elf
        calories = []

    # if valid values, append to current elf's bag
    else:
        calories.append(int(line))

# max
print(max(sum_of_calories))

# PART TWO

# sort the bag in descending order
sum_of_calories.sort(reverse=True)
# sum first 3 elements (max 3)
print(sum(sum_of_calories[0:3]))
