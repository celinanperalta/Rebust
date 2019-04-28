from datamuse import datamuse
from clarifai.rest import ClarifaiApp, Workflow
import re, heapq
import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')



class Rebust:

    MAX_RESULTS = 5
    MAX_WORD_RESULTS = 10

    def __init__(self):
        self.api = datamuse.Datamuse()
        self.app = ClarifaiApp(api_key='efac6c485194474790aa9732ed895aa2')
        self.workflow = Workflow(self.app.api, workflow_id="rebus-workflow")

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

    def get_syllables(self,word):
        word = word.lower()
        count = 0
        vowels = "aeiouy"
        if word[0] in vowels:
            count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
        if word.endswith("e"):
            count -= 1
        if count == 0:
            count += 1
        return count

    def get_sounds_like(self, word, n_syll):

        res = self.api.words(sl=word, v='enwiki', max=self.MAX_RESULTS)
        ret = []
        # print("Similar sound to: " + word)
        for w in res:
            if wordnet.synsets(w['word']):
                if(self.get_syllables(w['word']) <= n_syll):
                    heapq.heappush(ret, (w['score'], w['word']))

        top_results = []

        for i in heapq.nlargest(self.MAX_RESULTS, ret):
            top_results.append(i[1])

        return top_results

    def get_image_predictions(self, type, img):
        response = None
        if type == "url":
            response = self.workflow.predict_by_url(img)
        else:
            response = self.workflow.predict_by_filename(img)

        results = []

        for m in response["results"][0]["outputs"]:
            for x in m["data"]["concepts"]:
                heapq.heappush(results, (x["value"], x["name"]))

        top_results = []

        for i in heapq.nlargest(5, results):
            if self.get_syllables(i[1]) <= 3:
                top_results.append(i[1])

        return top_results

    def generate_combos(self, tokens):
        arr = []
        for tk in tokens:
            # print(tk)
            if not isinstance(tk, list):
                arr.append(tk)
            elif isinstance(tk, list):
                if len(arr) == 0:
                    for x in tk:
                        arr.append(x)
                else:
                    tmp = []
                    for x in arr:
                        for y in tk:
                            tmp.append(x + y)
                    arr = tmp.copy()

        return arr


    def solve_word(self, word):
        tokens = []
        for x in word:
            if x[0] == "str":
                tokens.append(x[1])
            elif x[0] == "img":
                tokens.append(self.get_image_predictions("img", x[1]))
            elif x[0] == "url":
                tokens.append(self.get_image_predictions("url", x[1]))

        #run through list, if there is a list of words, see what makes the most sense
        poss = self.generate_combos(tokens)
        poss = poss[0:self.MAX_WORD_RESULTS]

        final = []

        for x in poss:
            res = self.get_sounds_like(x, 5)
            if res != None:
                final += res[0:3]

        return final[0:self.MAX_WORD_RESULTS]

    #this gon be a big boy
    def parse_rebus(self, rebus):
        guess = []
        #rebus input should be tuple (type, [str or (img_type, img)]
        for word in rebus:
            guess.append(self.solve_word(word))

        return guess


