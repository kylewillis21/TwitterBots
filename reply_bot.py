import accessToken
import tweepy
import logging
import time
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# This function will go through all of your mentions and reply to any of them containg a keyword provided
def check_mentions(api, keywords, since_id):
    logger.info("Looking for mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering to, {tweet.user.name}")
            
            #If you want the account to follow them if the account does not already follow them
            #if not tweet.user.following:
                #tweet.user.follow()
            
            api.update_status(
                status = "reply given", # This will be the reply given to the user
                in_reply_to_status_id = tweet.id,
                auto_populate_reply_metadata=True
            )
    return new_since_id

def main():
    
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(accessToken.CONSUMER_KEY, accessToken.CONSUMER_SECRET) # These are retrieved from the accessToken file
    auth.set_access_token(accessToken.ACCESS_TOKEN, accessToken.ACCESS_SECRET)
    
    # Create an API object
    api = tweepy.API(auth)
    
    since_id = 1
    while True:
        since_id = check_mentions(api, ["keyword"], since_id) #The array contains keywords that the bot will be looking for in replys
        logger.info("Waiting...")
        time.sleep(30) # Timer used so that the program is not constantly running and sending too many requests

if __name__ == "__main__":
    main()
    
