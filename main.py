
# Python program to read
# json file
 
 
import json
 
# Asumming data set in root directory with same name
f = open('farmers-protest-tweets-2021-03-5.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)

def mostretweeted(tweets=data):
    #createing and id retweets hashmap
    tweets_rank = dict()
    for tweet in tweets:
        if len(tweets_rank.keys() <10):
            tweets_rank[tweet[str(len(tweets_rank.keys()))]] = [tweet['id'], tweet['retweetCount']]
        else:
            for rank in range(10):
                if tweet['retweetCount'] > tweets_rank[str(rank)][1]:
                    tweets_rank[str(rank)] = [tweet['id'], tweet['retweetCount']]

    print('Most retweeted tweets are:')
    for tweet in tweets_rank:
        print(f'Tweet id: {tweet[0]} retweets:{ tweet[1]}')

def main():
    print("Ejercicio 1")
    mostretweeted()
    print("Ejercicio 2")
