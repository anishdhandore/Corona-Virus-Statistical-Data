import requests
import json
from pprint import pprint
from datetime import date


def display(country):


    url = "https://rapidapi.p.rapidapi.com/country"

    #country = str(input("Enter the country you want to search for: "))
    querystring = {"name": country}

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "7852f8c452msh3232b768e72c928p1294a2jsn8400d801ea96"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()

    code = data[0]["code"]
    country_name = data[0]["country"]
    confirmed = data[0]["confirmed"]
    deaths = data[0]["deaths"]
    critical = data[0]["critical"]
    recovered = data[0]["recovered"]
    latest_update = data[0]["lastUpdate"]


    data = {
        'code' : data[0]["code"],
        'country_name' : data[0]["country"],
        'confirmed' : data[0]["confirmed"],
        'deaths' : data[0]["deaths"],
        'critical' : data[0]["critical"],
        'recovered' : data[0]["recovered"],
        'latest_update' : data[0]["lastUpdate"]


    }
    return data
    #return '''
    #{} has {} cases,
    #Deaths : {},
    #Critical : {},
    #Recovered : {},
    #Updated on : {}'''.format(country_name,confirmed,deaths,critical,recovered,latest_update)












    #return code,country_name,confirmed,deaths,critical,recovered,latest_update
