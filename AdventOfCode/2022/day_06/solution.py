MARKER_LENGTH = 4
MARKER_LENGTH_2 = 14

# read the input file
with open("input.txt", "r") as input_file:
    data = input_file.read()
    data = data.strip()

def get_marker(data, marker_length):
    # take the string
    for index, char in enumerate(data):
        # capture 4 characters
        packet = data[index: index+marker_length]
        
        # check if there are duplicates
        if len(set(packet)) == marker_length or index + marker_length == len(data) :
            break

    print(index + marker_length, len(data))

get_marker(data, MARKER_LENGTH)

# PART TWO

get_marker(data, MARKER_LENGTH_2)
