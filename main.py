from flask import Flask, flash, redirect, render_template, request, send_from_directory
from datamuse import datamuse
from werkzeug.utils import secure_filename
import logging
import os
import validators
from rebust import Rebust

logging.basicConfig(level=logging.DEBUG)

UPLOAD_FOLDER = os.path.basename('uploads')

app = Flask(__name__)
api = datamuse.Datamuse()
app.secret_key = 'buttttttts'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXT = set(['png', 'jpg', 'jpeg', 'txt'])



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXT

@app.route("/rhymes/<string:word>/")
def rhymes(word):
    word_rhy = api.words(sl=word, max=5)
    return render_template('rhymes.html',word_rhy=word_rhy)

@app.route('/', methods = ['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        word_num = 0
        words = [[]]
        inputs = int(request.form["size"][request.form["size"].index("-")+1:])
        print(inputs)
        for i in range(1, inputs+1):
            if request.form.get(str(word_num)+"-"+str(i), default="") == "":
                try:
                    file = request.files[str(word_num)+"-"+str(i)]
                    filename = secure_filename(file.filename)
                    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(full_filename)
                    words[word_num].append(("img", (full_filename[full_filename.rindex(".")+1:], full_filename)))
                except:
                    words.append([])
                    word_num += 1

            else:
                str_type = "str"
                if validators.url(request.form[str(word_num)+"-"+str(i)]):
                    str_type = "url"
                words[word_num].append((str_type, request.form[str(word_num)+"-"+str(i)]))


        # if file:
        #     filename = secure_filename(file.filename)
        #     full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        #     file.save(full_filename)
        rebust = Rebust()
        print(words)
        rebust.parse_rebus(words)
        return render_template('index.html')
    else:
        return render_template('index.html')

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/yay1', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.lower()
    return processed_text

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug = True)