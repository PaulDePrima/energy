from flask import Flask, url_for, render_template, request, Markup, flash
import os, json, random

app = Flask(__name__)

with open('energy.json') as energy_data:
    energy = json.load(energy_data)

@app.route("/")
def render_main():
    return render_template('Home.html')
    
@app.route("/facts")
def render_second():
    return render_template('facts.html', year = get_year_options())

@app.route("/UsImprt2")
def render_usprts2():
       us_imp = request.args["year"]
       print(us_imp)
       return render_template('facts.html', year = get_year_options(us_imp))
    
@app.route("/export")
def render_third():
    return render_template('exports.html')
    
@app.route("/consume")
def render_four():
    return render_template('consume.html')

def get_year_options(default = None):
    options = ""
    state = ""
    for c in energy:
        if not str(c["year"]) == state:
            if str(c["year"]) == default:
              options += Markup("<option selected value=\"" + default + "\">" + default + "</option>")
              print('true')
            else:
              options += Markup("<option value=\"" + str(c["year"]) + "\">" + str(c["year"]) + "</option>")
            state = str(c["year"])

    return options

def us_importEngery(year):
       imprts = energy[1949-year]["imports"]
       randKey = random.choice(list(imprts.keys()))

       return randKey + ": " + imprts[randKey] + " Quadrillion BTUs"
    
    

if __name__=="__main__":
    app.run(debug=True, port=54321)
