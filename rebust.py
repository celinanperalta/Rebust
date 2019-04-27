from datamuse import datamuse
from clarifai.rest import ClarifaiApp, Workflow
import re, heapq

class Rebust:

    MAX_RESULTS = 10
    MAX_WORD_RESULTS = 5

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

    def get_sounds_like(self, word):

        res = self.api.words(sl=word, v='enwiki', max=self.MAX_RESULTS)
        ret = []
        # print("Similar sound to: " + word)
        for w in res:
            ret.append(w['word'])
        # print("---------------------------------------")

        return ret

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
                tokens.append(self.get_image_predictions(x[1][0], x[1][1]))

        #run through list, if there is a list of words, see what makes the most sense
        poss = self.generate_combos(tokens)
        poss = poss[0:self.MAX_WORD_RESULTS]

        final = []

        for x in poss:
            res = self.get_sounds_like(x)
            if res != None:
                final += res[0:3]

        return final

    #this gon be a big boy
    def parse_rebus(self, rebus):

        guess = []
        #rebus input should be tuple (type, [str or (img_type, img)]
        for word in rebus:
            guess += self.solve_word(word)


