import requests
import pytest
def test_1():
    url = "http://localhost:5000/"
    resp = requests.get(url).text
    assert resp == 'test_passed'

test_1()