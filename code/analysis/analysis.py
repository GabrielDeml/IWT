import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
import requests
import operator


class analysis:

    search_words = ["trophy", "skin"
                "fur",
                "dragon",
                "pelt",
                "tusk",
                "ivory",
                "scale",
                "taxidermy",
                "rug",
                "hide",
                "bone",
                "meat",
                "delicacy",
                "medicine",
                "live",
                "pangolin",
                "leopard",
                "rhino",
                "sungazer",
                "lizard",
                "crocodile",
                "alligator",
                "parrot",
                "snake",
                "python",
                "yellow material",
                "white plastic",
                "jelly",
                "aloo",
                "kola",
                "australian teddy bear",
                "stripped t-shirt",
                "four wheeler",
                "antique",
                "mammoth",
                "carved",
                "sale",
                "selling",
                "price",
                "xiangya",
                "african material",
                "ANTEBELLUMELEG1"]

    def load_tweets(file_path: str):
        """
        Loads tweets from a JSON file.

        @param file_path: path to the JSON file
        @return: Loaded json file
        """

        with open(file_path, 'r') as f:
            return json.load(f)

    def print_tweet(tweet: str):
        """
        Prints a tweet.

        @param tweet: tweet to print
        """

        print(json.dumps(tweet, indent=4))
    
    def get_tweet_text(tweet: str):
        """
        Gets the text of a tweet.
        
        @param tweet: tweet to get the text from
        @return: text of the tweet
        """

        return tweet['text']
    
    def get_tweet_id(tweet: str):
        """
        Gets the id of a tweet.
        
        @param tweet: tweet to get the id from
        @return: id of the tweet
        """

        return tweet['id']

    def get_tweet_user(tweet: str):
        """
        Gets the user of a tweet.

        @param tweet: tweet to get the user from
        @return: user of the tweet
        """

        return tweet['user']

    def get_tweet_confidence(tweet: str):
        """
        Gets the confidence of a tweet.

        @param tweet: tweet to get the confidence from
        @return: confidence of the tweet
        """
        return tweet['confidence']

    def search_for_words(tweets: list, search_words: list):
        """
        Searches for words in a list of tweets.

        @param tweets: list of tweets
        @param search_words: list of words to search for
        @return: list of tweets containing the search words
        @return: number of tweets containing the search words
        @return: total number of tweets
        @return: number of times a search words appears the list of tweets
        """
        suspicious_tweets_word_list = []
        tweets_with_search_words = []
        suspicious_tweet_count = 0
        total_tweet_count = 0
        suspicious_tweets_word_count = {}
        for tweet in tweets:
            total_tweet_count += 1
            for search_word in search_words:
                if search_word in tweet.lower():
                    if tweet_suspicious == False:
                        tweet['suspicious_word'] = [search_word]
                        suspicious_tweets_word_list.append([search_word])
                        suspicious_tweet_count += 1
                    else:
                        suspicious_tweets_word_list[-1].append(search_word)
                        tweet['suspicious_word'].append(search_word)
                    tweet_suspicious = True
                    suspicious_tweets_word_count[search_word] += 1
        if len(tweet) > 0:
            tweets_with_search_words.append(tweet)

        return tweets_with_search_words, suspicious_tweet_count, total_tweet_count, suspicious_tweets_word_count
