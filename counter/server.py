from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = 'Secret'
@app.route('/')

def index():
  if 'counter' not in session:
      session['counter'] = 1
  else:
      session['counter']+=1
  return render_template("index.html")

@app.route('/addtwo', methods=['POST'])

def addtwo(): 
    session['counter']+=2
    return render_template("index.html")

@app.route('/reset', methods=['POST'])

def reset():
    session['counter'] = 0
    return render_template("index.html")

app.run(debug=True)