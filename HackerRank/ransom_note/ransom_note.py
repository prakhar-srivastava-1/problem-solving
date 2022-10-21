"""
Harold is a kidnapper who wrote a ransom note, 
but now he is worried it will be traced back to 
him through his handwriting. He found a magazine 
and wants to know if he can cut out whole words 
from it and use them to create an untraceable 
replica of his ransom note. The words in his note 
are case-sensitive and he must use only whole words 
available in the magazine. He cannot use substrings 
or concatenation to create the words he needs.

Given the words in the magazine and the words in the 
ransom note, print Yes if he can replicate his ransom 
note exactly using whole words from the magazine; 
otherwise, print No.
"""

def check_words(counters, note):
    for word in note.split():
        if word in counters.keys():
            if counters[word] > 0: 
                counters[word] -= 1 
            else:
                return False
        else:
            return False

def checkMagazine(magazine, note):
    ctr = 0
    counters = {}
    magazine_words = magazine.split()

    for key in magazine_words:
        counters[key] = counters.get(key, 0) + 1
    print(counters)
       
    
    if check_words(counters, note):
        print('Yes')
    else:
        print('No')

checkMagazine("attack at dawn", "Attack at dawn")