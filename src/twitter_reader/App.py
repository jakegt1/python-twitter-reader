from twitter_reader.Config import twitter
from twitter_reader.Twitter import TwitterAPI
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template(
        "index.html"
    )

