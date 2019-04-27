from datamuse import datamuse
import re

class Rebust:

    MAX_RESULTS = 20

    def __init__(self):
        self.api = datamuse.Datamuse()

    #given an array of strings and operators, concat individual rebus word
    def concat_word(self, rebus):
        word = re.split(" ", rebus)
        str = ""
        for i in range(0, len(word)):
           if word[i] == "-":
               str = str.replace(word[i+1], '', 1)
               i += 2
           elif word[i] != "+" and word[i-1] != "-":
               str += word[i]
        return str

    def get_sounds_like(self, word):
        print("Similar sound to: " + word)
        for w in self.api.words(sl=word, v='enwiki', max=self.MAX_RESULTS):
            print(w['word'])
        print("---------------------------------------")

    def image_to_word(self, img):
        return -1



