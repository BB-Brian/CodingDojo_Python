from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/ninjas')
def ninjas():
  return render_template('ninjas.html')

@app.route('/dojos')
def dojos():
  return render_template('dojos.html')

@app.route('/new', methods=['POST'])
def create_user():

   name = request.form['name']
   email = request.form['email']
   print name
   print email
   return redirect('/')

app.run(debug=True)
