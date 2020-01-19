import twitter
import json

api = twitter.Api(
    consumer_key='置き換える',
    consumer_secret='置き換える',
    access_token_key='置き換える',
    access_token_secret='置き換える',
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