"""
Sherlock considers a string to be valid if all characters 
of the string appear the same number of times. It is also 
valid if he can remove just  character at  index in the 
string, and the remaining characters will occur the same 
number of times. Given a string , determine if it is valid. 
If so, return YES, otherwise return NO.
"""
x

def test_isValid():
    test_cases = [
        ('abc', 'YES'),
        ('abcc', 'YES'),
        ('abc', 'YES'),
        ('aabbcd', 'NO'),
        ('aabbccddeefghi', 'NO'),
        ('abcdefghhgfedecba', 'YES'),
        ('aabbc', 'YES'),
        ('ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd', 'YES')
    ]

    ctr = 1
    results = []

    for test_case in test_cases:
        print(f'Test Case #{ctr}:')
        result = isValid(test_case[0])

        if result == test_case[1]:
            print('Test PASSED')
        else:
            print('Test FAILED')
            results.append(ctr)
        ctr += 1
        print('===============================')

    print(f'Failed Cases: {results}')
    
    
test_isValid()