import sched, tweepy
import time as time_module
import accessToken

# Authenticate to Twitter
auth = tweepy.OAuthHandler(accessToken.CONSUMER_KEY, accessToken.CONSUMER_SECRET)
auth.set_access_token(accessToken.ACCESS_TOKEN, accessToken.ACCESS_SECRET)

# Create API object
api = tweepy.API(auth)

# Create a tweet function
def tweet():
    api.update_status("Message")

# Create a scheduler function that runs the tweet program at specified time
scheduler = sched.scheduler(time_module.time, time_module.sleep)
t = time_module.strptime('2020-02-29 12:11:00', '%Y-%m-%d %H:%M:%S') # Enter the time and date that you would like the tweet to go out
t = time_module.mktime(t)
scheduler_e = scheduler.enterabs(t, 1, tweet, ())
scheduler.run()


                    



