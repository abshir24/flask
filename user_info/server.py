from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')

def index():
  return render_template("index.html")

@app.route('/info', methods=['POST'])

def info():
    return render_template('info.html',userinfo=request.form)

app.run(debug=True)