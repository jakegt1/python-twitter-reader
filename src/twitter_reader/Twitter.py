from oauth2 import Consumer, Token, Client
import json

class TwitterAPI():
    def __init__(self, consumer_key, consumer_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.format_url = 'https://api.twitter.com/1.1/{}'

    def oauth_request(
        self,
        url,
        key,
        secret,
        http_method="GET",
        http_headers=None
    ):
        consumer = Consumer(key=self.consumer_key, secret=self.consumer_secret)
        token = Token(key=key, secret=secret)
        client = Client(consumer, token)
        resp, content = client.request(
            url,
            method=http_method,
            headers=http_headers
        )
        return content

    def get_tweets_from_user(self, username, key, secret, limit=10):
        search_url = self.format_url.format('search/tweets.json?')
        search_url += 'q=from:' + username + '&'
        search_url += 'count=' + str(limit)
        print(search_url)
        return json.loads(self.oauth_request(search_url, key, secret).decode("utf-8"))

class User():
    def __init__(self, user_json):
        self.name = None
        self.profile_image = None
        self.username = None
        self.link = None
        if(user_json):
            data_dict = self.make_user(user_json)
            self.name = data_dict["name"]
            self.profile_image = data_dict["profile_image"]
            self.username = data_dict["username"]
            self.link = data_dict["link"]

    def make_user(self, user_json):
        data = {}
        data["name"] = user_json.get("name")
        data["profile_image"] = user_json.get("profile_image_url")
        data["username"] = user_json.get("screen_name")
        data["link"] = "http://twitter.com/"+data["username"]
        return data

    def to_dict(self):
        dict = {
            "name": self.name,
            "profile_image": self.profile_image,
            "username": self.username,
            "link": self.link
        }
        return dict


class Tweet():
    def __init__(self, tweet_json):
        data_dict = self.make_tweet(tweet_json)
        self.user = data_dict["user"]
        self.text = data_dict["text"]
        self.url = data_dict["url"]
        self.hashtags = data_dict["hashtags"]
        self.retweets = data_dict["retweets"]
        self.favourites = data_dict["favourites"]
        self.creation_date = data_dict["creation_date"]

    def make_tweet(self, tweet_json):
        data = {}
        data["user"] = User(tweet_json.get("user"))
        data["text"] = tweet_json.get("text")
        data["url"] = None
        data["hashtags"] = None
        entities = tweet_json.get("entities")
        if(entities):
            hashtags = entities.get("hashtags")
            if(hashtags):
                data["hashtags"] = [
                    hashtag["text"]
                    for hashtag in
                    hashtags
                ]
            urls = entities.get("urls")
            if(urls):
                data["url"] = urls[0].get("url")
        data["retweets"] = tweet_json.get("retweet_count")
        data["favourites"] = tweet_json.get("favourite_count")
        data["creation_date"] = tweet_json.get("created_at")
        return data

    def to_dict(self):
        dict = {
            "user": self.user.to_dict(),
            "text": self.text,
            "url": self.url,
            "hashtags": self.hashtags,
            "retweets": self.retweets,
            "favourites": self.favourites,
            "creation_date": self.creation_date
        }
        return dict

    def __str__(self):
        return str(self.to_dict())



