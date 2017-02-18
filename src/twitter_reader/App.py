from twitter_reader.Config import twitter
from twitter_reader.Twitter import TwitterAPI, Tweet, User
from flask import Flask, render_template
import re
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
            access_secret,
            20
        )
    return get_tweets_from_user

get_tweets_from_user = get_tweets_from_user_closure(
    twitter_handler,
    twitter["access_token"],
    twitter["access_secret"]
)

pp = pprint.PrettyPrinter(indent=4)

def make_urls_from_text(tweet_text):
    at_mention = "<a href='https://twitter.com/{}'>@{}</a>"
    regex_at_mentions = re.compile(r'@([\w]+)')
    all_at_mentions = regex_at_mentions.finditer(tweet_text)
    for match in all_at_mentions:
        formatted_mention = at_mention.format(
            match.group(1),
            match.group(1)
        )
        tweet_text = tweet_text.replace(match.group(0), formatted_mention)
    hashtag = "<a href='https://twitter.com/hashtag/{}'>#{}</a>"
    regex_hashtag = re.compile(r'#([\w]+)')
    all_hashtags = regex_hashtag.finditer(tweet_text)
    for match in all_hashtags:
        formatted_hashtag = hashtag.format(
            match.group(1),
            match.group(1)
        )
        tweet_text = tweet_text.replace(match.group(0), formatted_hashtag)
    return tweet_text



app = Flask(__name__)
@app.route("/")
def index():
    response_content = get_tweets_from_user('MaplecroftRisk')
    statuses =response_content["statuses"]
    tweets = [Tweet(tweet) for tweet in statuses]
    for tweet in tweets:
        tweet.text = make_urls_from_text(tweet.text)
    statuses = [status["text"] for status in statuses]
    return render_template(
        "index.html",
        tweet_list = tweets
    )

