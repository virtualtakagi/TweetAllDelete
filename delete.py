import twitter
import json

api = twitter.Api(
    consumer_key='�u��������',
    consumer_secret='�u��������',
    access_token_key='�u��������',
    access_token_secret='�u��������',
    sleep_on_rate_limit=True
)

with open('tweet.js', encoding='utf-8', mode='r') as f:
	tj=json.load(f)
	for tweet in tj:
		print(tweet['tweet']['id'])
		try:
			api.DestroyStatus(tweet['tweet']['id'])
		except Exception as e:
			print(e.args)