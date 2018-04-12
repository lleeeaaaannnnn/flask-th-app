from flask import Flask, render_template, redirect, url_for, request, make_response, flash
import json
from options import DEFAULTS


app = Flask(__name__)
app.secret_key = 'abc123'

def get_saved_data():
    try:
	    data = json.loads(request.cookies.get('character'))  #returns dict
    except TypeError:
	    data = {}
    return data

@app.route('/')
def index():
    return render_template("index.html", saves=get_saved_data())

@app.route('/builder')
def builder():
    return render_template('builder.html', saves=get_saved_data(),
    options=DEFAULTS)



@app.route('/save',methods=['POST'])
def save():
    #import pdb; pdb.set_trace()
    flash("Nice one!") 
    response = make_response(redirect(url_for('builder')))
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('character',json.dumps(data))
    return response

app.run(debug=True)
