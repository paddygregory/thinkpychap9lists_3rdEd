def anagram(Word1,Word2):
    one=list(Word1)
    two=list(Word2)
    if sorted(one) == sorted(two):
         print(Word1, "and", Word2, "are anagrams")

#anagram("listen", "silent")

fin=open('word.txt')
for line in fin:
    word = line.strip()
    # anagram('takes', word)


# EXERCISE TWO
def is_palindrome(word):
    if word == ''.join(reversed(word)):
        return True
    return False

 
#is_palindrome('rotator')

def file():
    fin=open('word.txt')
    for line in fin:
        word = line.strip()
        if len(word) > 7 and is_palindrome(word):
            print(word, "is a palindrome")

#file()

# EXERCISE THREE
def reverse_sentence(word):
    word_list = word.split()
    reversed_list = word_list[::-1]
    return ' '.join(reversed_list)

#print(reverse_sentence('reverse this sentence'))

# EXERCISE FOUR
word_list = []
for line in open('word.txt'):
    word = line.strip()
    word_list.append(word)
    letters = len(word_list)
print(letters)
















    