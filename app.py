from flask import Flask, redirect, session, make_response, flash, jsonify, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes
c = CurrencyRates()
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

fcurr =''
tcurr =''
amount = 0

@app.route("/")
def base():
    # session[RESPONSES] = []
    

    country = c.get_rates('USD') 
    print(type(country))
    return render_template("index.html", country=country)

@app.route('/get', methods=['POST'])
def get_convert():
    fcurr = request.form['fcurr']
    tcurr = request.form['tcurr']
    amount = request.form['amount']

    if(fcurr is ""):
        return redirect("/")
    if(tcurr is ""):
        return redirect("/")
    if(amount.isdigit() == 'False'):
        return redirect("/")
 
    session['fcurr'] = fcurr
    session['tcurr'] = tcurr
    session['amount'] = amount
    
    return  redirect("/results")

@app.route('/results')
def make_convert():
    
    fcurr = session['fcurr']
    tcurr =  str(session['tcurr'])
    amount =  int(session['amount'])


    str1 = str(f"'{fcurr}'")
    str2 = f"'{tcurr}'"
    
    
    # total = c.convert(str1,str2, amount)
    # I get an error saying Currency Rates Source Not Ready
    # this is because I cannot pass str1. I tried changing it into a string, dictionary, list, json, and nothing.

    return  render_template("results.html", fcurr=fcurr, tcurr=tcurr, amount=amount)