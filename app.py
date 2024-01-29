from flask import Flask

app = Flask(__name__)

@app.route('/')
def return_string():
    return "test_passed"
