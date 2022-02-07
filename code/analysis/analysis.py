import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
import requests
import operator
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from multiprocessing import Pool


class analysis:

    bad_word_list = ["trophy",
                     "skin"
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

    def load_json(file_path: str):
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
        suspicious_words_in_tweets = {}
        for search_word in search_words:
            suspicious_words_in_tweets[search_word] = 0
        for tweet in tweets:
            tweet_text = analysis.get_tweet_text(tweet)
            total_tweet_count += 1
            tweet_suspicious = False
            for search_word in search_words:
                if search_word in tweet_text.lower():
                    if tweet_suspicious == False:
                        tweet['suspicious_word'] = [search_word]
                        suspicious_tweets_word_list.append(search_word)
                        suspicious_tweet_count += 1
                    else:
                        suspicious_tweets_word_list.append(search_word)
                        tweet['suspicious_word'].append(search_word)
                        tweet_suspicious = True
                    suspicious_words_in_tweets[search_word] += 1
            if tweet_suspicious:
                tweets_with_search_words.append(tweet)

        return tweets_with_search_words, suspicious_tweet_count, total_tweet_count, suspicious_words_in_tweets

    def text_cleaner(tweet: dict):

        # Set up stopwords
        table = str.maketrans('', '', string.punctuation)
        stop = stopwords.words('english')
        lemmatizer = WordNetLemmatizer()
        tweet_text = analysis.get_tweet_text(tweet)
        tweet_text = ' '.join([word for word in tweet_text.lower(
        ).split() if word not in stop])  # remove stopwords
        tweet_text = tweet_text.translate(table)  # remove punc.
        tweet_text = ''.join(
            c for c in tweet_text if not c.isdigit())  # remove numbers
        tweet_text = tweet_text.replace(
            '  ', ' ')  # remove double spaces
        tweet_text = ' '.join([lemmatizer.lemmatize(word)
                               for word in tweet_text.split()])  # lemminize
        tweet["text"] = tweet_text
        return tweet

    def clean_tweets(tweets: list):
        """
        Clean tweets text.

        @param tweets: list of tweets
        @return: list of cleaned tweets
        """

        # Set up nltk
        nltk.download('stopwords')
        nltk.download('wordnet')
        nltk.download('omw-1.4')

        # Get number of cpu threads
        num_threads = os.cpu_count()
        with Pool(processes=num_threads) as pool:
            tweets = pool.map(analysis.text_cleaner, tweets)

        return tweets

    def find_bigrams_from_tweets(tweets: list):
        """
        Creates bigrams from tweets.

        @param tweets: list of tweets
        @return: bigrams
        """
        # Merge all tweets into one string
        tweets_text = "".join([analysis.get_tweet_text(tweet)
                              for tweet in tweets])
        return nltk.bigrams(tweets_text.split())

    def get_top_bigrams(bigram, num_bigrams):
        """
        Get the top n bigrams.
        
        @param bigram: bigrams
        @param num_bigrams: number of bigrams to get
        @return: top n bigrams
        """
        bigram_count = nltk.FreqDist(bigram)
        return bigram_count.most_common(num_bigrams)
