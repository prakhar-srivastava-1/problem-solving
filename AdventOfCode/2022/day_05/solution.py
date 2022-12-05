import re

# read the input
with open("input.txt", "r") as input_file:
    data = input_file.read()
    data = data.split("\n")

# add the configuration
"""   
            [J]             [B] [W]
            [T]     [W] [F] [R] [Z]
        [Q] [M]     [J] [R] [W] [H]
    [F] [L] [P]     [R] [N] [Z] [G]
[F] [M] [S] [Q]     [M] [P] [S] [C]
[L] [V] [R] [V] [W] [P] [C] [P] [J]
[M] [Z] [V] [S] [S] [V] [Q] [H] [M]
[W] [B] [H] [F] [L] [F] [J] [V] [B]
 1   2   3   4   5   6   7   8   9 
 """
stacks = [
    [],
    list('WMLF'),
    list('BZVMF'),
    list('HVRSLQ'),
    list('FSVQPMTJ'),
    list('LSW'),
    list('FVPMRJW'),
    list('JQCPNRF'),
    list('VHPSZWRB'),
    list('BMJCGHZW'),
]

# to save queries for part two
all_queries = []

# parse queries
for each_query in data:
    each_query = each_query.strip()

    # capture digits from line
    query_list = re.findall("\d+", each_query)

    # capture number of moves
    n = int(query_list[0])

    # capture source
    s = int(query_list[1])

    # capture destination
    d = int(query_list[2])
    
    # append to all_queries
    all_queries.append((n, s, d))

    while n != 0:
        stacks[d].append(stacks[s].pop())
        n -= 1
    
crates = [stack[-1] for stack in stacks[1:] if len(stack) > 0]
print(''.join(crates))

# PART TWO

# re-configure 
stacks = [
    [],
    list('WMLF'),
    list('BZVMF'),
    list('HVRSLQ'),
    list('FSVQPMTJ'),
    list('LSW'),
    list('FVPMRJW'),
    list('JQCPNRF'),
    list('VHPSZWRB'),
    list('BMJCGHZW'),
]

# parse queries
for each_query in all_queries:
    n, s, d = each_query

    # append to stack
    stacks[d] = stacks[d] + stacks[s][len(stacks[s]) - n:]

    # remove from stack
    stacks[s][:] = stacks[s][:-n] if len(stacks[s]) != n else []

crates = [stack[-1] for stack in stacks[1:] if len(stack) > 0]
print(''.join(crates))