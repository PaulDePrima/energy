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
    return render_template('facts.html')
    
@app.route("/export")
def render_third():
    return render_template('exports.html')
    
@app.route("/consume")
def render_four():
    return render_template('consume.html')

if __name__=="__main__":
    app.run(debug=True, port=54321)
