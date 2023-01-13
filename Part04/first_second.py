sentence = "it was a dark and stormy python"  # this is the string

def first_word(sentence):
    for i in range(0, len(sentence)):
        if " " == sentence[i]:
            for j in range(0, i):
                print(sentence[j], end="")
            break

def second_word(sentence):
    k = 0
    for i in range(0, len(sentence)):
        if " " == sentence[i]:
            k = k + 1
            if k == 2:
                for j in range(0, i):
                    print(sentence[j], end="")

first_word(sentence)
print()

# The solution was provided from stackoverflow :)
# sentence.split() will return a list of all the words that are separated by whitespace:
def firstWord(sentence):
    return sentence.split()[0]

def secondWord(sentence):
    return sentence.split()[1]

def lastWord(sentence):
    return sentence.split()[-1]


if __name__ == "__main__":
    sentence = "I want to learn python"
    print(firstWord(sentence))
    print(secondWord(sentence))
    print(lastWord(sentence))

if __name__ == "__main__":
    sentence = "deneme iki 3"
    print(firstWord(sentence))
    print(secondWord(sentence))
    print(lastWord(sentence))