from flask import Flask
import sys
import random
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/about')
def about():
    return 'The about page'