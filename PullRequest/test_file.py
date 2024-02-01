""" testing for the return string from the flask server """

import requests
def test_1():
    """ the actual test """
    url = "http://flask_server:5000/"
    resp = requests.get(url, timeout=10).text
    print("Testing now")
    assert resp == 'test_passed'

test_1()
