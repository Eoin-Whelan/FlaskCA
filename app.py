"""
Title:		webApp.py
Author:	Eoin Farrell
Student No:	C00164354
Purpose:	webApp.py provides the Flask Controller for the website.
DOC:		30/10/2020
"""

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def display_homepage():
    return render_template("index.html", main_title="The Eoin Zone")


@app.route("/personalPage")
def personalPage():
    return render_template("personalPage.html", main_title="About Me!")


@app.route("/CV")
def cv():
    return render_template("resume.html", main_title="Professional Details")


@app.route("/techInterests")
def techInterests():
    return render_template("techinterests.html", main_title="What Draws Me To Soft. Engineering")


@app.route("/assistiveTech")
def assistiveTech():
    return render_template("assistiveTech.html", main_title="Assistive Technology")
