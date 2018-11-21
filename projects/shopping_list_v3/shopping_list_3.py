from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from flask import make_response
from flask import send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
   return send_from_directory('static',"shopping_list2.html")

@app.route('/save', methods=['GET', 'POST'])
def flask_save():
   if request.method == 'POST':

       pass

@app.route('/get', methods=['GET', 'POST'])
def flask_get():
   if request.method == 'GET':
       pass