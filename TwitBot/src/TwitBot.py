from tweepy import OAuthHandler
from settings import *
import tweepy, json, sys, random, discord

client = discord.Client()

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
    
api = tweepy.API(auth, wait_on_rate_limit=True)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!twitter'):
        print(message.content)
        query = message.content.replace('!twitter ', '')
        max_tweets = 20
        searched_tweets = [status for status in tweepy.Cursor(api.search, q=query, lang='en', retweeted=False).items(max_tweets)]
        
        post = random.choice(searched_tweets)._json['text'].encode(sys.getdefaultencoding(),errors='replace')
        post = post.decode('utf-8')
        print(post)
        await client.send_message(message.channel, post)
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

