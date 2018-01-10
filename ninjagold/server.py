from flask import Flask, render_template, request, redirect,session
import random
app = Flask(__name__)
app.secret_key = 'Secret'
@app.route('/')

def index():
  session['messages'] = [] 
  if 'gold' not in session:
      session['gold'] = 0
  return render_template("index.html")


@app.route('/process_money', methods=['POST'])

def process():
    if request.form['building'] == 'farm':
        gold = random.randrange(10, 21)
        session['gold'] += gold
        session['messages'].append("You earned {} gold!".format(gold))
    
    elif request.form['building'] == 'cave':
        gold = random.randrange(5, 11) 
        session['gold'] += gold
        session['messages'].append("You earned {} gold!".format(gold))
    
    elif request.form['building'] == 'house':
        gold = random.randrange(2, 6)
        session['gold'] += gold
        session['messages'].append("You earned {} gold!".format(gold))
    
    else:
        gold = random.randrange(0, 51)
        randomint = random.randrange(0, 2)
        if randomint:
            session['gold'] += gold
            session['messages'].append("You earned {} gold!".format(gold))
        else:
            session['gold'] -= gold
            session['messages'].append("You lost {} gold!".format(gold))
    return render_template("index.html")

app.run(debug=True)