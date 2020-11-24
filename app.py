"""
Title:		app.py
Author:	Eoin Farrell
Student No:	C00164354
DOC:		30/10/2020
"""

from flask import Flask, render_template, request
from data_utils import save_data, get_data

app = Flask(__name__)

"""
    For display_homepage, it has an additional ovveride of the basic function
    so that when the user enters their information their information on the
    guestbook, their name is displayed back to them with an alternative greeting.
"""


@app.route("/")
def display_homepage():
    return render_template(
        "index.html",
        main_title="The Eoin Zone",
        pageHeaderMsg="",
        userName="Visitor",
        open_message="If you would be so kind as to sign the guestbook before continuing, I would be so grateful",
        data= get_data()
    )


def display_homepage(guest_Signed="Stranger"):
    return render_template(
        "index.html",
        main_title="The Eoin Zone",
        userName=guest_Signed,
        open_message="Feel free to check out this website through the menu above!",
        data= get_data()
    )


"""
    /processForm appends the comments.txt file and returns the user to the
    homepage with a personalized greeting. If they choose not to enter their name,
    a default name "Stranger" is assigned to them in their greeting.
"""


@app.route("/processForm", methods=["POST"])
def process_form_data():
    data = request.form
    save_data(data)
    if data["userName"] == "":
        return display_homepage()
    return display_homepage(data["userName"])


@app.route("/personalPage")
def personalPage():
    return render_template(
        "personalPage.html",
        main_title="About Me!",
        pageHeaderMsg="You want to know about me!?",
    )


@app.route("/CV")
def cv():
    return render_template("CV.html", main_title="Professional Details")


@app.route("/techHub")
def techInterests():
    return render_template(
        "techHub.html", main_title="What Draws Me To Soft. Engineering"
    )


@app.route("/assistiveTech")
def assistiveTech():
    return render_template("assistiveTech.html", main_title="Assistive Tech!")


@app.route("/arduino")
def arduino():
    return render_template("arduino.html", main_title="The Power of Uno!")


@app.route("/VR")
def VR():
    return render_template("virtualReality.html", main_title="VR!")


@app.route("/personalInterests")
def personalInterests():
    return render_template("personalInterests.html", main_title="Personal Interests!")
