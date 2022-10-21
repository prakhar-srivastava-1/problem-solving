"""
You will be given a list of integers, arr, and a single 
integer k. You must create an array of length  from 
elements of  such that its unfairness is minimized. 
Call that array arr'. Unfairness of an array is calculated 
as
            
             max(arr') - min(arr')

Where:
- max denotes the largest integer in 
- min denotes the smallest integer in 
"""

SENTINEL = 1000000001

def maxMin(k, arr):
    print("k = ", k)
    print("len(arr) = ", len(arr))
    # if duplicates => return 0
    # if len(arr) > len(list(set(arr))):
    #     return 0
    
    # sort the arrray
    arr.sort()
    # print(arr)
    
    # take differences of pairs
    min_num = SENTINEL
    
    for i in range(len(arr) - k):
        diff = max(arr[i:i+k]) - min(arr[i:i+k])
        # print(arr[i:i+k], min_num, diff)
        if min_num > diff:
            min_num = diff
        
    return min_num

n = int(input())
k = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

print(maxMin(k, arr))