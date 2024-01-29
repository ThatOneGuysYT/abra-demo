import requests

def test1():
    url = "http://localhost:5001/"
    resp = requests.get(url).text
    assert resp == 'test_passed'

test1()