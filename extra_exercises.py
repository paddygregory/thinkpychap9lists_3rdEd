def uses_all(word,required):
    i = 0 
    while i<len(required):
        if required[i] not in word:
            return False
        i = i + 1
    return True

#print(uses_all('hello','eoh'))
print(uses_all('hello','eohz'))
