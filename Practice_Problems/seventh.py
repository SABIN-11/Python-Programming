# calculate the frequency of the words in a sentence
# "the cat sat on the mat the cat" → {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}

def freq_ctr(sentence: str) -> dict:

    sentence = sentence.lower()
    li = sentence.split()
    di = {}

    for i in li:
        if i not in di:
            di[i] = 1
        else:
            di[i] += 1

    return di

sen = input("Enter a sentence: ")
print(f"Frequency count is as follows:\n{freq_ctr(sen)}")
