"""
A student is taking a cryptography class and has found 
anagrams to be very useful. Two strings are anagrams of 
each other if the first string's letters can be rearranged 
to form the second string. In other words, both strings 
must contain the same exact letters in the same exact 
frequency. For example, bacdc and dcbac are anagrams, but 
bacdc and dcbad are not.
The student decides on an encryption scheme that involves 
two large strings. The encryption is dependent on the 
minimum number of character deletions required to make the 
two strings anagrams. Determine this number.
Given two strings,  and , that may or may not be of the 
same length, determine the minimum number of character 
deletions required to make  and  anagrams. Any characters 
can be deleted from either of the strings.
"""

def get_sum(dict_a, dict_b):
    total = 0
    for key in dict_a.keys():
        total += min(dict_a[key], dict_b[key])
    return total * 2


def makeAnagram(a, b):
    # Write your code here
    list_a, list_b = list(a), list(b) 
    dict_a, dict_b = {}, {}
    set_a, set_b = set(list(a)), set(list(b))
    set_c = set_a.intersection(set_b)

    print(set_a, set_b, set_c)
    for each in set_c:
        dict_a[each] = list_a.count(each)
        dict_b[each] = list_b.count(each)
    
    print(dict_a, dict_b)
    print(get_sum(dict_a, dict_b))
    print(len(a)+ len(b) - get_sum(dict_a, dict_b))

def test_makeAnagram():
    test_cases = [
        ("cde", "abc"),
        ("cde", "dcf"),
    ]
    for test_case in test_cases:
        makeAnagram(test_case[0], test_case[1])

test_makeAnagram()