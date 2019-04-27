from datamuse import datamuse
import re

api = datamuse.Datamuse()

#given an array of strings and operators, concat individual rebus word
def concat_word(word):
    str = ""
    for i in range(0, len(word)):
       if word[i] == "-":
           str = str.replace(word[i+1], '', 1)
           i += 2
       elif word[i] != "+" and word[i-1] != "-":
           str += word[i]

    return str

def get_sl(word):
    print("Similar sound to: " + word)
    for w in api.words(sl=word, v='enwiki', max=20):
        print(w['word'])
    print("---------------------------------------")

# def image_to_word(img):


str = re.split(" ", input("Enter a rebus word: "))
print(str)

get_sl(concat_word(str))


