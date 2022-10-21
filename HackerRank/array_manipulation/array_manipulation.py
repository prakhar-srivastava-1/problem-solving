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
    arr = [0] * n

    # check each query
    for query in queries:
        # perform query and update original array
        arr = perform_query(arr, query)
        # print(arr)
    
    # return maximum element
    return(max(arr))

def test_arrayManipulation():
    test_cases = (
        {'n': 5, 'queries':[[1, 2, 100], [2, 5, 100], [3, 4, 100]]}
    )

    print(arrayManipulation(test_cases['n'], test_cases['queries']))

test_arrayManipulation()