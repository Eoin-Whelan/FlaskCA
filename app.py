"""
Title:		    app.py
Author:	        Eoin Farrell
Student No:	    C00164354
DOC:		    30/10/2020
CA2 Update:     24/11/2020
"""

from flask import Flask, render_template, request
from data_utils import save_data, get_data

app = Flask(__name__)

#   Render functions for each page on personal site.
@app.route("/")
def display_homepage():
    return render_template(
        "index.html",
        metaTitle="homePage",
        main_title="The Eoin Zone",
        pageHeaderMsg="",
        userName="Visitor",
        open_message="If you would be so kind as to sign the guestbook before continuing, I would be so grateful",
        data=get_data(),
    )


def display_homepage(guest_Signed="Stranger"):
    """
        display_homepage overload in the event a visitor signs the guestbook
        without a name.
    """
    return render_template(
        "index.html",
        metaTitle="homePage",
        main_title="The Eoin Zone",
        userName=guest_Signed,
        open_message="Feel free to check out this website through the menu above!",
        data=get_data(),
    )


@app.route("/processForm", methods=["POST"])
def process_form_data():
    """
        processForm gathers form data, calls the save_data function from data_utils,
        saving the signature to the database and returns the user to the homepage.
    """
    data = request.form
    save_data(data)
    if data["userName"] == "":
        return display_homepage()
    return display_homepage(data["userName"])


@app.route("/personalPage")
def personalPage():
    return render_template(
        "personalPage.html",
        metaTitle="aboutMe",
        main_title="About Me!",
        pageHeaderMsg="You want to know about me!?",
    )


@app.route("/CV")
def cv():
    return render_template("CV.html", metaTitle="cv", main_title="Professional Details")


@app.route("/techHub")
def techInterests():
    return render_template(
        "techHub.html",
        metaTitle="techHub",
        main_title="What Draws Me To Soft. Engineering",
    )


@app.route("/assistiveTech")
def assistiveTech():
    return render_template(
        "assistiveTech.html", metaTitle="assistiveTech", main_title="Assistive Tech!"
    )


@app.route("/arduino")
def arduino():
    return render_template(
        "arduino.html", metaTitle="arduino", main_title="The Power of Uno!"
    )


@app.route("/VR")
def VR():
    return render_template("virtualReality.html", metaTitle="VR", main_title="VR!")


@app.route("/personalInterests")
def personalInterests():
    return render_template(
        "personalInterests.html",
        metaTitle="personalInterests",
        main_title="Personal Interests!",
    )
