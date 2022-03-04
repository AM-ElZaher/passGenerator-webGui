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
    length = request.form.get('passCount')
    
    if request.method == 'POST':
        pwdlength = int(length)
        spStat = request.form.get('chkSp')
        nmStat = request.form.get('chkNm')
        btStat = request.form.get('chkBoth')
        # pwd = (''.join(random.choice(numbs + lowers + sym) for i in range(pwdlength)))
        if ((str(spStat)) != "None") and ((str(nmStat)) != "None") and ((str(btStat)) != "None"):
            print("invalid")



        if (str(spStat)) != "None":
            pwd = (''.join(random.choice(lowers + sym) for i in range(pwdlength)))
            return render_template('index.html', genPass=pwd)

        elif (str(nmStat)) != "None":
            pwd = (''.join(random.choice(numbs + lowers) for i in range(pwdlength)))
            return render_template('index.html', genPass=pwd)

        elif ((str(btStat)) != "None"):
            pwd = (''.join(random.choice(numbs + lowers + sym) for i in range(pwdlength)))
            return render_template('index.html', genPass=pwd)

        else:
            pwd = (''.join(random.choice(lowers) for i in range(pwdlength)))
        return render_template('index.html', genPass=pwd)
    else:
        return render_template('index.html')
    


