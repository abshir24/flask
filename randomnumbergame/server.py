from flask import Flask, render_template, request, redirect,session
import random
app = Flask(__name__)
app.secret_key = 'Secret'
@app.route('/')

def index():
    session['message']= ""
    session['randomnumber'] = random.randrange(0, 101)
    return render_template("index.html")

@app.route('/guess', methods=['POST'])

def guess():
    if int(request.form['guess']) == session['randomnumber']:    
        session['message'] = 'Correct! Your number was {}'.format(session['randomnumber'])
    
    elif int(request.form['guess']) > session['randomnumber']:
        session['message'] = 'Too High!'

    elif int(request.form['guess']) < session['randomnumber']:
        session['message'] = 'Too Low!'

    return render_template("index.html")




app.run(debug=True)