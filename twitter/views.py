from django.http import HttpResponse
from dotenv.main import dotenv_values
import tweepy


def index(request):
    dotenv_config = dotenv_values(".env")
    token = dotenv_config["BEARER_TOKEN"]
    api = tweepy.Client(bearer_token=token)
    tweet = api.get_tweet(id='1408095468723318784')

    return HttpResponse(tweet)
