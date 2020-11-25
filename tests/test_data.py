"""
    Title:          test_data.py
    Author:         Eoin Farrell
    Student Number: C00164354
    Purpose:        Tests to automatically perform on data_utils
    DOC:            24/11/2020
"""

import DBcm
from data_utils import get_data, save_data


def test_database_data_format():
    """
        Test checks that result set is of type list. If so, that the list is
        entirely composed of tuples.
    """
    data = get_data()
    if len(data) > 0:
        assert isinstance(data, list) == True
        for entry in data:
            assert isinstance(entry, tuple) == True


def test_data_cols():
    """
        Test ensures get_data() is only returning the number of desired columns
        from the database.
    """
    data = get_data()
    if len(data) > 0:
        assert len(data[0]) == 2


def test_insert_signature(clean_insertion):
    """
        insert_signature checks to see if the insertion method of data_utils
        can successfully complete and upon completion, issues a deletion statement
        to remove the test record from the table.
    """
    record = {"userEmail": "testEntry", "userMsg": "testMsg"}
    current_table_length = len(get_data())
    save_data(record)
    new_data_set = get_data()
    test_data_cols()
    test_database_data_format()
    assert len(get_data()) == current_table_length + 1
    assert new_data_set[0][0] == record["userEmail"]
    assert new_data_set[0][1] == record["userMsg"]
