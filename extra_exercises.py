def uses_all(word,required):
    i = 0 
    while i<len(required):
        if required[i] not in word:
            return False
        i = i + 1
    return True

#print(uses_all('hello','eoh'))
# print(uses_all('hello','eohz'))

# EX. TWO

def check_word(word,available,required):
    if len(word)<4:
        return False
    if required not in word:
        return False
    for letter in word:
        if letter not in available:
            return False
    return True

list1 = ['o','a','c','r','t']
#print(check_word('ratat', list1, 'r'))
#print(check_word('razat', 'oalsh', 'r'))

def score_word(word, available):
    for letter in available:
        if letter not in word:
            return len(word)
    return len(word) + 7

listone = ['r', 'a', 't', 'a', 't', 'a']
#print(score_word('ratata', listone))  # Should print 13

    # EX. THREE

def uses_none(word, forbidden):
    for letter in forbidden:
        if letter in word:
            return False
    return True

#print(uses_none('banana', 'xyz') )
#print(uses_none('banana', 'bxyz') ) 
