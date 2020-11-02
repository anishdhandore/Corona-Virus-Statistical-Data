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

    data = display(user_country)

    cases =(str(data['country_name']) + " has " + str(data['confirmed']) + " cases. ")
    deaths = ("Deaths: "+ str(data['deaths']))
    critical = ("Critical: "+ str(data['critical']))
    recovered = ("Recovered: " + str(data['recovered']))
    updated = ("Last updated on: " + data['latest_update'])



    return render_template(
        'result.html',
        country=user_country,
        cases = cases,
        deaths = deaths,
        critical = critical,
        recovered = recovered,
        updated = updated

    )

if __name__=="__main__":
    app.run(debug=True)








#pprint(data)





#display(code,country_name,confirmed,deaths,critical,recovered,latest_update)
