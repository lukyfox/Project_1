from flask import Flask
from flask import redirect, url_for, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/index/<name>')
def hello_world(name):
    return redirect(url_for('getUserPage', name='Lukas', surname='Florner'))
    #return 'Hello World!'

@app.route('/mypage/<surname>_<name>')
def getUserPage(name, surname):
    return render_template('user.html', name = name, surname=surname)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    #return 'Hello World!'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404