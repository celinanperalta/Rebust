from flask import Flask, flash, redirect, render_template, request, session, abort
from datamuse import datamuse

app = Flask(__name__)
api = datamuse.Datamuse()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/rhymes/<string:word>/")
def rhymes(word):
    word_rhy = api.words(sl=word, max=5)
    return render_template('rhymes.html',word_rhy=word_rhy)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)