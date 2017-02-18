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


