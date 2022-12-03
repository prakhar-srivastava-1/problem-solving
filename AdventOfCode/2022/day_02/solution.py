# initialize dictionaries for part one

# element wise score
scores = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

# win cases
win_list = [
    ['A', 'Y'],
    ['B', 'Z'],
    ['C', 'X']
]

# draw cases
draw_list = [
    ['A', 'X'],
    ['B', 'Y'],
    ['C', 'Z']
]

# read the input
with open("input.txt", "r") as input_file:
    data = input_file.read()
    data = data.split("\n")

# cumulative counter for tracking score
score = 0
for each_round in data:
    this_round = each_round.split()
    
    # win cases
    if this_round in win_list:
        score += 6 + scores[this_round[-1]]
    
    # draw cases
    elif this_round in draw_list:
        score += 3 + scores[this_round[-1]]
    
    # loss cases
    else:
        score += scores[this_round[-1]]

# output     
print(score)

# PART TWO
# initialize dictionaries for part two

# result score based on char in input
scores_round = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

# element wise score
scores_elements = {
    'A': 1,
    'B': 2,
    'C': 3
}

# win moves (mapped to same char set)
win_dict = {
    'A': 'B',
    'B': 'C',
    'C': 'A',
}

# draw moves (mapped to same char set)
draw_dict = {
    'A': 'A',
    'B': 'B',
    'C': 'C',
}

# loss moves (mapped to same char set)
loss_dict = {
    'A': 'C',
    'B': 'A',
    'C': 'B',
}

# tracker for part two score
score_2 = 0
for each_round in data:
    this_round = each_round.split()
    
    # get the round result
    result = this_round[1]
    # get the result_score
    result_score = scores_round[result]
    # add to score for this part
    score_2 += result_score

    # get chosen element
    # loss
    if result == 'X':
        choice = loss_dict[this_round[0]]
    # win
    elif result == 'Z':
        choice = win_dict[this_round[0]]
    # draw
    else:
        choice = draw_dict[this_round[0]]
    
    # add to score for this part
    score_2 += scores_elements[choice] 
          
print(score_2)


