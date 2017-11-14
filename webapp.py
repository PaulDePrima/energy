from flask import Flask, url_for, render_template, request, Markup, flash
import os, json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('Home.html')

if __name__=="__main__":
    app.run(debug=False, port=54321)
