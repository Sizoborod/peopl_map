from flask import Flask, render_template, request
import flask_restful

from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from waitress import serve
from werkzeug.utils import redirect

from flask_restful import reqparse, abort, Api, Resource
from translation import up


up()
app = Flask(__name__)
api = flask_restful.Api(app)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

'''login_manager = LoginManager()
login_manager.init_app(app)'''



@app.route('/')
def main_window():
    return render_template('object_manager.html')

@app.route("/map")
def map():
    map_pars = {}
    return render_template("geo.html")

@app.route("/map2")
def map2():
    map_pars = {}
    return render_template("object_manager.html")



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
    '''serve(app, host='0.0.0.0', port=5000)'''