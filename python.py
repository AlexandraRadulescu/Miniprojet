from flask import Flask, render_template, request
from wtforms import Form, FloatField
import random

app = Flask(__name__)  

@app.route('/')
def home():
    return render_template('index.html', random=None)

@app.route('/makerand', methods=['GET', 'POST'])
def makerand():
    r=random.randint(0,100)
    return render_template('index.html', random=r)
   
if __name__ == '__main__':
    app.run(debug=True)
