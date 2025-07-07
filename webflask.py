import flask
import requests
import pandas
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Swapnanil is always gay"

if __name__ == "__main__":
    app.run(debug=True)