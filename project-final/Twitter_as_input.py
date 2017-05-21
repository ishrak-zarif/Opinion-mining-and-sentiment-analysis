from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import project.sentiment_mod as s


ckey = "3Bfqolbvk1KaMXd1eksDgU1Ol"
csecret = "K1PIMz6BsA0LkoIRGDxG6gDddIk6RpSWsvMwVs9y3dYJBsaGu1"
atoken = "3314407080-DbW4DyHyEqR2dWpsgFfZ4g4dbKNA0JYTOtADq5E"
asecret = "BHT85bW2NiA4e4GCpxpSxiqqhxDUqHxyX8z0pdzXIufaQ"


class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        sentiment_value= s.sentiment(tweet)
        print(tweet, sentiment_value)


        output = open("twitter_out.txt","a")
        output.write(sentiment_value)
        output.write('\n')
        output.close()

        return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)


twitterStream = Stream(auth, listener())
twitterStream.filter(track=["trump"])
