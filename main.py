import requests
import json
from pprint import pprint
from datetime import date

#for flask
from flask import Flask, render_template, flash, request, redirect
from functions import *
#from keys import *

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method=="POST":
        country = request.form.get('country')
        
    return render_template('index.html')

@app.route("/result", methods = ["GET", "POST"])
def result():
    user_country = request.args.get('country', None)

    name = display(user_country)
    

    return render_template('result.html', country=user_country, data=data)

if __name__=="__main__":
    app.run(debug=True)








#pprint(data)





#display(code,country_name,confirmed,deaths,critical,recovered,latest_update)


