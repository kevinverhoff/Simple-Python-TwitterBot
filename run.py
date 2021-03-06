#!/usr/local/bin/python2.7
import tweepy
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener, Stream
from tweepy.auth import OAuthHandler

ckey = ''
csecret = ''
atoken = ''
asecret = ''

auths = OAuthHandler(ckey, csecret)
auths.set_access_token(atoken, asecret)
api = tweepy.API(auths)

class listener(StreamListener):
    def on_data(self, raw_data):
        try:
            tweet_text = raw_data.lower().split('"text":"')[1].split('","source":"')[0].replace(",", "") #tweet's text
            screen_name = raw_data.lower().split('"screen_name":"')[1].split('","location"')[0].replace(",", "") #tweet's authors screen name
            tweet_sid = raw_data.split('"id":')[1].split('"id_str":')[0].replace(",", "") #tweet's id

			#whitelist handles and words goes in here
            whitelist_acc = ['', '']
            whitelist_words = ['', '']

            #banned handles and words goes in here
            banned_accs =  [' ' ,' ']
            banned_words = ['Dirtbike' ,'ATV','motorcycle']

            if not any(a_acc == screen_name.lower() for a_acc in whitelist_acc):
                if not any(acc == screen_name.lower() for acc in banned_accs):
                    if not any(a_wrds in screen_name.lower() for a_wrds in whitelist_words):
                        if not any(word in tweet_text.lower() for word in banned_words):
                            #call what u want to do here
                            #for example :
                            #fav(tweet_sid)
                            retweet(tweet_sid)
                    else:
                        #call what u want to do here
                        #for example :
                        #fav(tweet_sid)
                        retweet(tweet_sid)
            else:
                #call what u want to do here
                #for example :
                #fav(tweet_sid)
                retweet(tweet_sid)
            return True
        except Exception as e:
            print(str(e)) # prints the error msg, if u dont want it comment it out
            pass

    def on_error(self, status_code):
        try:
            print( "error " + status_code)
        except Exception as e:
            print(str(e))
        pass


def retweet(tweet_sid):
    try:
        api.retweet(tweet_sid)
    except Exception as e:
        print(str(e))
        pass


def fav(tweet_sid):
    try:
        api.create_favorite(tweet_sid)
    except Exception as e:
        print(str(e))
        pass

track_words = ['NJCycling','NJ Cycling','NewJersey Cycling','NJ Bike','NJBike'] #Whatever you want to retweet should go here.
follow_acc = ['19401785'] #retweets every tweet from this accounts, handles converted to ids

print("Running...")
try:
    twt = Stream(auths, listener())
    twt.filter(track= track_words) # or follow = follow_acc
except Exception as e:
    print(str(e))
    pass
