"""
    Title:          conftest.py
    Author:         Eoin Farrell
    Student Number: C00164354
    Purpose:        conftest.py consists of fixture functions in assisting data and application test files.
    DOC:            24/11/2020
"""

import pytest
import app as webapp
import DBcm

from data_utils import get_data

#   Credentials to access the DB to perform fixture functions such s clean_insertion.
testCredentials = {
    "host": "127.0.0.1",
    "user": "admin",
    "password": "deckard2019",
    "database": "guestBook",
}


@pytest.fixture
def clean_insertion():
    """
        clean_insertion is called to remove test data placed in the signatures table
        by exterior functions that perform inserts.
    """
    yield
    with DBcm.UseDatabase(testCredentials) as cursor:
        del_SQL = "DELETE FROM signatures WHERE guestEmail='testEntry'"
        cursor.execute(del_SQL)


#       beginning of web application testing.
@pytest.fixture
def app():
    app = webapp.app
    return app
