"""
    Title:          test_app.py
    Author:         Eoin Farrell
    Student Number: C00164354
    Purpose:        Set of tests for app.py
    DOC:            24/11/2020
"""


def test_up(client):
    """
        Tests that client can launch without error by ensuring a status_code of
        200 is returned.
    """
    assert client.get("/").status_code == 200


def test_site_pages(client):
    """
        test_site_pages contains a 2D list of active pages on the application.
        A <meta> tag identifies each page uniquely and is associated with the path
        to the site in flask. Each site in the active_URL_list is tested with a call
        and their corresponding <meta> tag.
        
        Any additional pages can be appended to this list in the format of:
          i) URL route ii) Unique meta tag.
    """
    active_URL_list = [
        ["/", "<meta name= homePage>"],
        ["/personalPage", "<meta name= aboutMe>"],
        ["/CV", "<meta name= cv>"],
        ["/techHub", "<meta name= techHub>"],
        ["/assistiveTech", "<meta name= assistiveTech>"],
        ["/arduino", "<meta name= arduino>"],
        ["/VR", "<meta name= VR>"],
        ["/personalInterests", "<meta name= personalInterests>"],
    ]
    for site in active_URL_list:
        reply = client.get(site[0])
        assert bytes(site[1], "utf8") in reply.data


def test_guestbook_sign(client):
    """
        test_guestbook_sign posts test data to the signatures table.
        The userEmail and userMsg match the data used in test_data.py's
        test_insert_signature function. This way ensures when the tests complete,
        conftest.py will finish clean_insertion function call and clean signatures
        table of all test data posted.

        Note: app_test_data's second dict contains a blank userName to test the
        overloaded function where a visitor chose not to enter a name.
    """
    app_test_data = [
        {"userName": "Guilfoyle", "userEmail": "testEntry", "userMsg": "testMsg"},
        {"userName": "", "userEmail": "testEntry", "userMsg": "testMsg"},
    ]
    for signature in app_test_data:
        print(type(signature))
        response = client.post("/processForm", data=signature)
        assert response.status_code == 200
        assert bytes(signature["userName"], "utf8") in response.data
