from datamuse import datamuse
from clarifai.rest import ClarifaiApp
import re

class Rebust:

    MAX_RESULTS = 20

    def __init__(self):
        self.api = datamuse.Datamuse()
        self.app = ClarifaiApp(api_key='efac6c485194474790aa9732ed895aa2')
        self.model = self.app.public_models.general_model

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

    def get_image_predictions(self, img):
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        response = None

        if re.match(regex, img) is not None:
            response = self.model.predict_by_url(img)
        else:
            response = self.model.predict_by_filename(img)

        results = response["outputs"][0]["data"]["concepts"]

        return results
