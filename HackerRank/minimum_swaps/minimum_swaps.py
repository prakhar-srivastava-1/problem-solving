"""
You are given an unordered array consisting of 
consecutive integers  [1, 2, 3, ..., n] without 
any duplicates. You are allowed to swap any two 
elements. Find the minimum number of swaps 
required to sort the array in ascending order.
"""

def test_minimumSwaps():
    test_cases = (
        [4, 3, 1, 2],
        [7, 1, 3, 2, 4, 5, 6] 
    )

    answers = [3, 5]
    calculated = []

    for case in test_cases:
        result = minimumSwaps(case)
        print(f"{case} => {result}")
        calculated.append(result)
    
    if calculated == answers:
        print("Test Cases passed successfully!")
    else:
        print(f"Tests failed!\nExpected: {answers}\nCalculated: {calculated}")


def minimumSwaps(arr):
    l = len(arr)

    # grab the first misplaced element
    arr_copy = arr.copy()
    arr_copy.sort()
    ctr = 0
    for i in range(l):
        if arr[i] != arr_copy[i]:
            ctr += 1
    
    return ctr - 1


test_minimumSwaps()

