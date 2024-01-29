import requests
import pytest

def test1():
    url = "https://reqres.in/api/users/2"
    resp = requests.get(url).json()["data"]['email']
    assert resp == 'janet.weaver@reqres.in'