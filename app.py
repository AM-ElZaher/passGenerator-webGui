from flask import Flask, render_template, request
import requests
import random
import string

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    lowers = string.ascii_letters
    numbs = string.digits
    sym = string.punctuation
    length = requester = request.form.get('passCount')
    if request.method == 'POST':
        pwdlength = int(length)
        pwd = (''.join(random.choice(numbs + lowers + sym) for i in range(pwdlength)))
        return render_template('index.html', genPass=pwd)
    else:
        return render_template('index.html')
    


