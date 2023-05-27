from requests_oauthlib import OAuth1Session
from dotenv import load_dotenv
import os
import json
import time
import datetime

load_dotenv()
consumer_key = os.environ.get("API_KEY")
consumer_secret = os.environ.get("API_KEY_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("TOKEN_SECRET")

# Oauth
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

def main():
    print("### Tweet Remover ###")
    with open("./tweet-remove.log", mode='a', encoding='utf-8') as f:
        dt = datetime.datetime.now()
        timestamp = dt.strftime('%Y/%m/%d %H:%M:%S')
        f.write("### " + timestamp + " ###\n")
    with open("./tweet-headers.json") as f:
        data = json.load(f)
    tweets = data["data"].copy()
    for cnt,tweetData in enumerate(reversed(tweets),1):
        tweet_id = tweetData["tweet"]["tweet_id"]
        print('No.' + str(cnt))
        print("Delete Tweet ID: " + str(tweet_id))
        # Request
        response = oauth.delete("https://api.twitter.com/2/tweets/{}".format(tweet_id))
        if response.status_code == 429:
            print("APIのリクエスト上限")
            with open("./tweet-remove.log", mode='a', encoding='utf-8') as f:
                f.write("Tweet_id: " + str(tweet_id) + "    Status: Too Many Requests\n")
            exit()
        elif response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(response.status_code, response.text)
            )
        print("Response code: {}".format(response.status_code))
        data["data"].remove(tweetData)
        with open("./tweet-headers.json", mode='w') as f:
            json.dump(data,f,indent=4)
        with open("./tweet-remove.log", mode='a', encoding='utf-8') as f:
            f.write("Tweet_id: " + str(tweet_id) + "    Status: " + response.status_code + '\n')
        time.sleep(1)
        if cnt >= 50:
            print("### 50 POST Done. ###")
            exit()
        

if __name__ == "__main__":
    main()