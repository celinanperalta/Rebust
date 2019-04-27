from flask import Flask, flash, redirect, render_template, request, session, abort
from datamuse import datamuse
from werkzeug import secure_filename

app = Flask(__name__)
api = datamuse.Datamuse()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/rhymes/<string:word>/")
def rhymes(word):
    word_rhy = api.words(sl=word, max=5)
    return render_template('rhymes.html',word_rhy=word_rhy)


@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded succcccccessfully bish'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug = True)