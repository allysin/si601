__author__ = 'grizzlemuff'

import oauth2 as oauth
import time
import json, urllib2

import requests

# Set the API endpoint
url = "https://api.twitter.com/1.1/search/tweets.json?q=bitcoin&lang=en"

# Set the base oauth_* parameters along with any other parameters required
# for the API call.
params = {
    'oauth_version': "1.0",
    'oauth_nonce': oauth.generate_nonce(),
    'oauth_timestamp': int(time.time()),
    }

# Set up instances of our Token and Consumer. The Consumer.key and
# Consumer.secret are given to you by the API provider. The Token.key and
# Token.secret is given to you after a three-legged authentication.
token = oauth.Token(key="2349415231-LXiSdwmrEL1yjWMVZItKPnlV28zSQ3Ihr5ozj96", secret="3y2Mail35Yx5nAua45AwSOrG2sNSIygzvhVlht9ebCZ2x")
consumer = oauth.Consumer(key="PTYHQOCXZUmT4R9Oljlg", secret="6mnfsOooZTNrFDF1N8Pf3LSN7NQSMsZudDdrDUwswIU")

# Set our token/key parameters
params['oauth_token'] = token.key
params['oauth_consumer_key'] = consumer.key

# Create our request. Change method, etc. accordingly.
req = oauth.Request(method="GET", url=url, parameters=params)

# Sign the request.
signature_method = oauth.SignatureMethod_HMAC_SHA1()
req.sign_request(signature_method, consumer, token)



punctuation=['!','@','.', ",","?"]
my_text = ''

complete_url='https://api.twitter.com/1.1/search/tweets.json?q=bitcoin&lang=en'
r = requests.get(complete_url)
tweets = r.json()
print tweets
