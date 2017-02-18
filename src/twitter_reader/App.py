from twitter_reader.Config import twitter
from twitter_reader.Twitter import TwitterAPI, Tweet, User
from flask import Flask, render_template
import pprint

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

pp = pprint.PrettyPrinter(indent=4)

app = Flask(__name__)
@app.route("/")
def index():
    response_content = get_tweets_from_user('MaplecroftRisk')
    statuses =response_content["statuses"]
    tweets = [Tweet(tweet) for tweet in statuses]
    pp.pprint(str(tweets[0]))
    statuses = [status["text"] for status in statuses]
    return render_template(
        "index.html",
        tweet_list = tweets
    )

