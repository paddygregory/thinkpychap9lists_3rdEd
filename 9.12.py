word_list = []
def words():
    for line in open('words.txt2'):
        word=line.strip()
        word_list.append(word)
    return len(word_list)

words()


