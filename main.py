import feedparser
import tweepy
import json
import os

RSS_URL = "https://leakedgems.com/forums/general-mega-pack.9/index.rss"
POSTED_FILE = "posted.json"

# Twitter API (X API v2)
auth = tweepy.OAuth1UserHandler(
    os.environ["API_KEY"],
    os.environ["API_SECRET"],
    os.environ["ACCESS_TOKEN"],
    os.environ["ACCESS_SECRET"]
)

api = tweepy.API(auth)

api.update_status("Test tweet working ✅")

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
