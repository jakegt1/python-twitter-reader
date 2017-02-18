from twitter_reader.Config import twitter
from twitter_reader.Twitter import TwitterAPI
from flask import Flask, render_template

twitter_handler = TwitterAPI(
    twitter["consumer_key"],
    twitter["consumer_secret"]
)

def get_tweets_from_user_closure(twitter, access_token, access_secret):
    def get_tweets_from_user(username):
        return twitter.get_tweets_from_user(
            username,
            access_token,
            access_secret
        )
    return get_tweets_from_user

get_tweets_from_user = get_tweets_from_user_closure(
    twitter_handler,
    twitter["access_token"],
    twitter["access_secret"]
)

app = Flask(__name__)
@app.route("/")
def index():
    response_content = get_tweets_from_user('MaplecroftRisk')
    statuses = response_content["statuses"]
    statuses = [status["text"] for status in statuses]
    return render_template(
        "index.html",
        my_statuses = statuses
    )

