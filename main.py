from flask import Flask, flash, redirect, render_template, request, url_for, session, abort
from datamuse import datamuse
from models import Info
from werkzeug.utils import secure_filename
import logging
import os
logging.basicConfig(level=logging.DEBUG)

UPLOAD_FOLDER = os.path.basename('uploads')

app = Flask(__name__)
api = datamuse.Datamuse()
app.secret_key = 'buttttttts'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXT = set(['png', 'jpg', 'jpeg', 'txt'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/",  methods =[ 'GET', 'POST'])
def index():
    if request.method == 'POST':
        data = Info(request.form['file'])
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('index.html')

@app.route("/rhymes/<string:word>/")
def rhymes(word):
    word_rhy = api.words(sl=word, max=5)
    return render_template('rhymes.html',word_rhy=word_rhy)

@app.route('/upload')
def upload_file():
    return render_template('index.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('ur dum')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('file uploaded succcccccessfully bish')
    return redirect('/upload')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug = True)