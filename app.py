"""
Title:		app.py
Author:	Eoin Farrell
Student No:	C00164354
DOC:		30/10/2020
"""

from flask import Flask, render_template, request


app = Flask(__name__)

"""
For display_homepage, it has an additional ovveride of the basic function
so that when the user enters their information their name is displayed back to
them with an alternative greeting.
"""

@app.route("/")
def display_homepage():
    return render_template(
        "index.html",
        main_title="The Eoin Zone",
        userName="Visitor",
        open_message="If you would be so kind as to sign the guestbook before continuing, I would be so grateful",
    )


def display_homepage(guest_Signed):
    return render_template(
        "index.html",
        main_title="The Eoin Zone",
        userName=guest_Signed,
        open_message="Thanks! Feel free to check out this website through the menu above!",
    )


@app.route("/processForm", methods=["POST"])
def process_form_data():
    data = request.form

    with open("comments.txt", "a") as df:
        print(data["userName"], ",", sep="", end="", file=df)
        print(data["userEmail"], ",", sep="", end="", file=df)
        print(data["userMsg"], ",", sep="", end="", file=df)
        df.write("\n")

    return display_homepage(data["userName"])


@app.route("/personalPage")
def personalPage():
    return render_template("personalPage.html", main_title="About Me!")


@app.route("/CV")
def cv():
    return render_template("resume.html", main_title="Professional Details")


@app.route("/techInterests")
def techInterests():
    return render_template(
        "techinterests.html", main_title="What Draws Me To Soft. Engineering"
    )


@app.route("/assistiveTech")
def assistiveTech():
    return render_template("assistiveTech.html", main_title="Assistive Technology")
