from flask import Flask, url_for, render_template, request, Markup, flash
import os, json, random

app = Flask(__name__)

with open('energy.json') as energy_data:
    energy = json.load(energy_data)

@app.route("/")
def render_main():
    return render_template('Home.html')
    
@app.route("/facts")
def render_usprts2():
	try:   
	    us_imp = request.args["year"]
	    return render_template('facts.html', year = get_year_options(us_imp), response = us_importEngery(us_imp))
	except:
		return render_template('facts.html', year = get_year_options())

	return render_template('importEnergy.html', year = get_year_options())
    
@app.route("/export")
def render_third():
	try:   
	    us_exp = request.args["year"]
	    return render_template('exports.html', year = get_year_options(us_exp), response = us_importEngery(us_exp))
	except:
		return render_template('exports.html', year = get_year_options())

    
@app.route("/consume")
def render_four():
        try:   
	    us_cons = request.args["year"]
	    return render_template('consume.html', year = get_year_options(us_cons), response = us_importEngery(us_cons))
        except:
		return render_template('consume.html', year = get_year_options())


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
       imprts = energy[1949-int(year)]["data"]["imports"]
       randKey = random.choice(list(imprts.keys()))

       return randKey + ": " + str(imprts[randKey]) + " Quadrillion BTUs"

    
    

if __name__=="__main__":
    app.run(debug=True, port=54321)
