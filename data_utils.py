"""
Title:		data_utils.py
Author:	Eoin Farrell
Student No:	C00164354
DOC:		24/11/2020
Purpose:    Handler for data to be passed from flask sites to SQL database..
"""


import DBcm


connection = {
    "host": "127.0.0.1",
    "user": "admin",
    "password": "deckard2019",
    "database": "guestBook",
}


def save_data(data):
    """
    save_data opens a connection to database and performs
    an insert using the information passed in through data.
    """
    with DBcm.UseDatabase(connection) as cursor:
        SQL = """ insert into signatures (guestEmail, guestComment)
                  values (%s, %s) """
        cursor.execute(SQL, (data["userEmail"], data["userMsg"]))


# 	Goes to DB, select * statement and returns the data retrieved.
def get_data():
    """ Retrieves all guest email and comment entries, ordering it by descending order so latest entries are returned first. """
    SQL = "select guestEmail, guestComment from signatures ORDER BY id DESC"
    with DBcm.UseDatabase(connection) as cursor:
        cursor.execute(SQL)
        data = cursor.fetchall()
    return data
