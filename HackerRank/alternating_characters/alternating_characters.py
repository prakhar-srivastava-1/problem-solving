"""
You are given a string containing characters  and  only. 
Your task is to change it into a string such that there 
are no matching adjacent characters. To do this, you are 
allowed to delete zero or more characters in the string.
Your task is to find the minimum number of required 
deletions.
"""
def alternatingCharacters(s):
    # Write your code here
    print(s)

    list_s = list(s)
    len_s = len(s)

    if len_s == list_s.count('A') or len_s == list_s.count('B'):
        return len(s) - 1
    
    # list_AB = s.split('AB')
    # list_BA = s.split('BA')
    # print(list_AB, list_BA)

    # total_AB = sum([len(x) for x in list_AB])
    # total_BA = sum([len(x) for x in list_BA])

    # return min(total_AB, total_BA)

    while 'AA' in s: 
        s = s.replace('AA', 'A')
    print("Replaced AA:\t", s)

    while 'BB' in s:
        s = s.replace('BB', 'B')
    print("Replaced BB:\t", s)

    return len_s - len(s)

def test_alternatingCharacters():
    test_cases = [
        'AAAA',
        'BBBBB',
        'ABABABAB',
        'BABABA',
        'AAABBB',
        'ABABABAA',
        'ABBABBAA',
    ]

    ctr = 1
    for test_case in test_cases:
        print(f'Test Case#{ctr}:')
        result = alternatingCharacters(test_case)
        print(f'{result}\n======================')
        ctr += 1

test_alternatingCharacters()