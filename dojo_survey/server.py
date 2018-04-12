from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['post'])
def create_user():
    print request.form
    name=request.form["name"]
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template('/results.html',name=name, location=location, language=language, comment=comment)

# @app.route('/results')
# def results():
#     return render_template('results.html')

@app.route('/goback', methods=['get'])
def goback():
    return redirect('/')



app.run(debug=True)




# from flask import Flask, render_template, request, redirect, session
# app = Flask(__name__)
# app.secret_key = 'What does this do?'
#
# @app.route('/')
# def index():
#     location_list = ['Jupiter','Seattle','Antarctica']
#     language_list = ['JavaScript','Python','MEAN','Robot']
#     return render_template('index.html', location_list = location_list, language_list = language_list)
#
# @app.route('/survey', methods=['post'])
# def create_user():
#     print request.form
#     session.name = request.form['name']
#     location = request.form['location']
#     language = request.form['language']
#     comment = request.form['comment']
#     return redirect('/results')
#
# @app.route('/results')
# def results():
#     return render_template('results.html')
#
# app.run(debug=True)
