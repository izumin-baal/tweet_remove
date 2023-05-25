from requests_oauthlib import OAuth1Session
from dotenv import load_dotenv
import os
import json
import time

# In your terminal please set your environment variables by running the following lines of code.
# export 'CONSUMER_KEY'='<your_consumer_key>'
# export 'CONSUMER_SECRET'='<your_consumer_secret>'

load_dotenv()
consumer_key = os.environ.get("API_KEY")
consumer_secret = os.environ.get("API_KEY_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("TOKEN_SECRET")

# Make the request
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

def main():
    print("### Tweet Remover ###")
    with open("./tweets.json") as f:
        data = json.load(f)
    tweets = data["tweet_id"].copy()
    for id in tweets:
        print("Delete Tweet ID: " + str(id))
        # Making the request
        response = oauth.delete("https://api.twitter.com/2/tweets/{}".format(id))

        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(response.status_code, response.text)
            )

        print("Response code: {}".format(response.status_code))

        # Saving the response as JSON
        json_response = response.json()
        print(json_response)
        data["tweet_id"].remove(id)
        with open("./tweets.json", mode='w') as f:
            json.dump(data,f,indent=4)
        

if __name__ == "__main__":
    main()