import feedparser
import tweepy
import json
import os

RSS_URL = "https://leakedgems.com/forums/general-mega-pack.9/index.rss"
POSTED_FILE = "posted.json"

# Twitter API (X API v2)
client = tweepy.Client(
    consumer_key=os.environ.get("ggIDSA1ZbNY5vknriB8k7pgApxoGYssZh7CuvdIYUtmfO"),
    consumer_secret=os.environ.get("Xx2Jd7dMf6CEMeSzcm8d8FgcC3zLD0onE3j2qODeSYj7gEMZlT"),
    access_token=os.environ.get("1937935395364257794-6rrVDrge8uypTT4ynyFFgcyV2pzmQw"),
    access_token_secret=os.environ.get("6uRsEAl2QmKuqwDUUTeY46UMUyWmBF6QrctiYwCah5RMW")
)

# Load already posted links
if os.path.exists(POSTED_FILE):
    with open(POSTED_FILE, "r") as f:
        posted = json.load(f)
else:
    posted = []

feed = feedparser.parse(RSS_URL)

new_posts = []

for entry in feed.entries[:5]:
    if entry.link not in posted:
        tweet = f"{entry.title}\n{entry.link}"
        try:
            client.create_tweet(text=tweet)
            print("Posted:", tweet)

            posted.append(entry.link)
            new_posts.append(entry.link)

        except Exception as e:
            print("Error:", e)

# Save updated posted list
with open(POSTED_FILE, "w") as f:
    json.dump(posted, f)
