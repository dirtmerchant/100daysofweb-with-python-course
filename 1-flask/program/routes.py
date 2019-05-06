from flask import render_template
from program import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/100Days')
def p100Days():
    return render_template('100Days.html')

@app.route('/notes')
def notes():
    return render_template('notes.html')

