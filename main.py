
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

def usersWithMostTweets(tweets=data):
    #creating a more useful hashmap id:count
    users = dict() 
    for tweet in tweets:
        if tweet['user']['id'] not in users.keys():
            users[tweet['user']['id']] = 1
        else:
            tweet['user']['id'] +=1
    top_users = []
    for user in users:
        if len(top_users) < 10:
            top_users.append(user)
        else:
            for i in range(10):
                if users[top_users[i]] < users[users]:
                    top_users[i] = user
                    break
    print('Users that tweet the most:')
    for user in top_users:
        print(f'User ID: {user} number of tweets: {users[user]}')


def datesWithMostTweets(tweets=data):
    #creating a more useful hashmap id:count
    dates = dict() 
    for tweet in tweets:
        if tweet['date']['id'] not in dates.keys():
            dates[tweet['date']['id']] = 1
        else:
            tweet['date']['id'] +=1
    top_dates = []
    for date in dates:
        if len(top_dates) < 10:
            top_dates.append(date)
        else:
            for i in range(10):
                if dates[top_dates[i]] < dates[dates]:
                    top_dates[i] = date
                    break
    print('dates that tweet the most:')
    for date in top_dates:
        print(f'date ID: {date} number of tweets: {dates[date]}')

def main():
    print("Ejercicio 1")
    mostretweeted()
    print("Ejercicio 2")
    usersWithMostTweets()
    print("Ejercicio 3")
    datesWithMostTweets()
