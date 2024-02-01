import requests
import pytest
def test_1():
    url = "http://flask_server:5000/"
    resp = requests.get(url).text
    print("Testing now")
    assert resp == 'test_passed'

test_1()
