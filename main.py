from flask import Flask
from flask import request
from flask import render_template
from werkzeug.exceptions import HTTPException


app = Flask(__name__)

@app.route("/")
def redirect():

    header_name = {'text': 'Главная - Успехи Киберзаучки'}
    output = render_template('index.html', header=header_name)
    return output

@app.route("/about")
def about():

    title_name = {'text': 'Инф. об Киберзаучке'}
    output = render_template('about.html', title=title_name)
    return output

@app.route("/index")
def index():

    header_name = {'text': 'Главная - Успехи Киберзаучки'}
    output = render_template('index.html', header=header_name)
    return output

@app.route("/contact")
def contact():

    main_name = {'text': 'Связь с Киберзаучкой'}
    output = render_template('contact.html', main=main_name)
    return output

@app.route("/sent", methods = ['GET', 'POST'])
def sent():
    if request.method == 'GET':
        return render_template('contact.html')
    else:
        print(request.json)
        return f'<h3>Saved</h3>'

@app.errorhandler(HTTPException)
def errors(e):
    res = e.description
    if e.code == 404:
        res = render_template('error404.html'), e.code
    elif e.code == 500:
        res = render_template('error500.html'), e.code
    return res
