from django.contrib import admin
from apitwitter.models import Tweet, TweetLike, TweetRetweet

admin.site.register(Tweet)
admin.site.register(TweetLike)
admin.site.register(TweetRetweet)
