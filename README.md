# Python twitter reader
This is a Python Flask webapp that takes the latest 10 tweets from a given user, lays them out on the page and shows where the posts were made if there was data for that.

## Requirements
* python3 (tested on 3.5.2)
* python3-pip
* wheel (pip3 install wheel)
* bower (for map-tools) (also requires nodejs and npm)
* OAuth tokens for single user sign on with [dev.twitter.com](https://dev.twitter.com/oauth/overview/single-user)

## Setup
NOTE: This assumes you are using some flavour of Linux.
### Config.py
Firstly, fill in Config.py (src/twitter_reader/Config.py). You will need your Consumer key, Consumer secret, access token and access secret which you can get from dev.twitter.com.
```python
twitter = {
  "consumer_key": "some_encoded_value_from_dev.twitter",
  "consumer_secret": ..
  ..
  "username": "username_of_twitter_account_you_want_to_scrape"
}
```
### Bower
Install bower with npm, ```npm install -g bower```. NOTE: This may return errors to do with node not existing - if this happens a simple fix of ```ln -s /usr/bin/nodejs /usr/bin/node``` should do the trick. 
Then simply run ```bower install``` which will add map-tools to the static directory of the webapp.
### Python3 dependencies
To install the python3 dependencies, whether in a virtualenv or not, do the following:
* ```pip3 install wheel``` (Needed for some packages)
* ```pip3 install -r requirements.txt```
This will install all python3 dependencies required for the webapp.

### Installing and running the app
Install the app by running ```python3 setup.py install```.
You can then start the web app using ```python3 -m twitter_reader```.

## Notes
This was developed using Bash for Windows, which effectively means Ubuntu 16.04.
