import tweepy
import csv

# Replace these values with your own
api_key = 'S84Tk8aPTP3D4IfbFh5wcnOWd'
api_secret_key = 'I5xK6aaTFzctgkhFE7an0KDmzGqvqclVDvTkvE0p1BubFW9Nfo'
access_token = '1906548597711388672-Fu0OWhPwlIoGzPGMei4gJNVfHKeBKp'
access_token_secret = 'xL415lBVmRddgy4BDDWSpvXnvmZYRW2poyL0jRQWLT6oO'

# Authenticate to Twitter
# auth = tweepy.OAuthHandler(api_key, api_secret_key)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)


# # Fetch tweets
# # Define the search query
# query = 'OpenAI OR ChatGPT OR "AI advancements" OR "prompt engineering" OR #OpenAI OR #ChatGPT OR #AI OR #ArtificialIntelligence OR #PromptEngineering OR #AIAchievements OR #GPT4 OR #MachineLearning'

# # Fetch tweets
# tweets = tweepy.Cursor(api.search_tweets, q=query, lang='en', tweet_mode='extended').items(1500)  # Adjust the number based on rate limits


# # Open/create a file to append data
# csv_file = open('./data/tweets.csv', 'a', newline='', encoding='utf-8')
# csv_writer = csv.writer(csv_file)

# # Write the header row
# csv_writer.writerow(['created_at', 'user', 'text'])

# # Write tweet data
# for tweet in tweets:
#     csv_writer.writerow([tweet.created_at, tweet.user.screen_name, tweet.full_text])

# csv_file.close()


# Use API v2 Endpoints --- Essential Access, 
# Authenticate to Twitter
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAPIr0QEAAAAAi2oZNwpOgojKP3QROD5L4rL1OIc%3DKfDKVtUmPKG7X7T9KaYaTXIWQv8D2wTtygGeiugLVeqk9gDKq7'
client = tweepy.Client(bearer_token=bearer_token)

# # Fetch tweets
query = 'OpenAI OR ChatGPT OR "AI advancements" OR "prompt engineering" OR #OpenAI OR #ChatGPT OR #AI OR #ArtificialIntelligence OR #PromptEngineering OR #AIAchievements OR #GPT4 OR #MachineLearning'
tweets = client.search_recent_tweets(query=query, max_results=400, tweet_fields=['created_at', 'author_id', 'text'])


# # Write tweet data
csv_file = open('./data/tweets.csv', 'a', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['created_at', 'author_id', 'text'])

for tweet in tweets.data:
    csv_writer.writerow([tweet.created_at, tweet.author_id, tweet.text])

csv_file.close()