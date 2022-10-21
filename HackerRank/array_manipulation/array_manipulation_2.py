"""
Starting with a 1-indexed array of zeros and 
a list of operations, for each operation add 
a value to each the array element between two 
given indices, inclusive. Once all operations 
have been performed, return the maximum value 
in the array.
"""
from operator import add

def perform_query(arr, query):
    start = query[0] - 1
    end = query[1] - 1
    addend = [query[2]] * (end-start+1)
    # for i in range(start, end+1):
    #     arr[i] += addend
    # print(list(map(add, arr[start:end+1], addend)))
    # print(arr[:start] + list(map(add, arr[start:end+1], addend)) + arr[end+1:])
    return arr[:start] + list(map(add, arr[start:end+1], addend)) + arr[end+1:]

def arrayManipulation(n, queries):
    # n sized array of zeros
    arr_dict = {}

    # check each query
    for query in queries:
        # perform query and update original array
        start = query[0] - 1
        end = query[1] - 1
        addend = query[2]
        # insert into dict
        for i in range(start, end+1):
            arr_dict[i] = arr_dict.get(i, 0) + addend

    return max(arr_dict.values())

def test_arrayManipulation():
    test_cases = [
        {'n': 5, 'queries':[[1, 2, 100], [2, 5, 100], [3, 4, 100]]},
        {'n': 10, 'queries':[[1, 5 , 3], [4, 8, 7], [6, 9, 1]]}
    ]

    for test_case in test_cases:
        print(arrayManipulation(test_case['n'], test_case['queries']))

test_arrayManipulation()