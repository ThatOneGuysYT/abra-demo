import requests
import pytest
def test_1():
    url = "http://flask_server:5000/"
    resp = requests.get(url).text
    assert resp == 'test_passed1'

test_1()