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
import pandas as pd
from sklearn.model_selection import train_test_split


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
        suspicious_words_in_tweets = {search_word: 0 for search_word in search_words}
        for tweet in tweets:
            tweet_text = analysis.get_tweet_text(tweet)
            total_tweet_count += 1
            tweet_suspicious = False
            for search_word in search_words:
                if search_word in tweet_text.lower():
                    if not tweet_suspicious:
                        tweet['suspicious_word'] = [search_word]
                        suspicious_tweets_word_list.append(search_word)
                        suspicious_tweet_count += 1
                        tweet_suspicious = True
                    else:
                        suspicious_tweets_word_list.append(search_word)
                        tweet['suspicious_word'].append(search_word)

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
        tweets_text = " ".join([analysis.get_tweet_text(tweet)
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
    
    def get_most_common_words(tweets: list, num_words: int = None):
        """
        Create a list of the most common words
        @param tweets: list of tweets
        @param num_words: number of words to get
        @return: list of most common words in a tuple (word, count)
        """
        # Merge all tweets into one string
        tweets_text = " ".join([analysis.get_tweet_text(tweet)
                                for tweet in tweets])
        word_count = nltk.FreqDist(tweets_text.split())
        if num_words is None:    
            return word_count.most_common()
        else:
            return word_count.most_common(num_words)

    def find_common_combinations_of_search_words(tweets: list, min_length: int):
        """
        Find the commin combinations of search words after running though search for words
        
        @param tweets: list of tweets
        @parm min_length: minimum length of the combination
        @return list of tuples with the search words first then the number of occurrences 
        """
        dict_of_tuples = {}
        for tweet in tweets:
            if len(tweet['suspicious_word']) >= min_length:
                # sort the list of suspicious words alphabetically
                sorted_suspicious_words = sorted(tweet['suspicious_word'])
                # Combine the sorted list of suspicious words into a string
                suspicious_words_string = ' '.join(sorted_suspicious_words)
                if suspicious_words_string in dict_of_tuples:
                    dict_of_tuples[suspicious_words_string] += 1
                else:
                    dict_of_tuples[suspicious_words_string] = 1

        out_list = [
            (item.split(), item_value)
            for item, item_value in dict_of_tuples.items()
        ]

        # Sort the list of tuples by the number of occurrences
        out_list = sorted(out_list, key=lambda x: x[-1], reverse=True)
        return out_list
    
    def universal_data_loader(file_path: str):
        """
        Load tweets form json file(s)
        
        @param file_path: Path to file(s)
        @return: list of tweets
        """
        
        tweets = []
        # Check if the file is a directory
        if os.path.isdir(file_path):
            for file in os.listdir(file_path):
                if file.endswith(".json"):
                    with open(file_path + file, 'r') as f:
                        tweets.append(json.load(f))
        else:
            # Load the single file
            with open(file_path, 'r') as f:
                tweets.append(json.load(f))
        return tweets
    
    
    def create_tweet_list_from_loaded_json(json_data):
        """
        Create a list of tweets from loaded json data
        
        @param json_data: dict json data
        @return: list of tweets
        """
        # Check if the json file is a list 
        if type(json_data) == list:
            # Check if the list is a list of tweets by looking for tweet text
                tweet_list = []
                for part in json_data:
                    tweet_list.extend(analysis.create_tweet_list_from_loaded_json(part))
                return tweet_list
        elif type(json_data) == dict:
            if 'tweet' in json_data:
                json_data['text'] = json_data['tweet']
                del json_data['tweet']
                return [json_data]
            if 'text' in json_data:
                return [json_data]
            # Go though the values and check if they are tweets
            tweet_list = []
            for value in json_data.values():
                tweet_list.extend(analysis.create_tweet_list_from_loaded_json(value))
            return tweet_list
        else:
            return []
        
    def create_bar_chart(data: list, num_of_items: int, x_label : str, y_label : str, title : str, file_name : str = None):
        """
        Create a bar chart from a list of tuples
        
        @param data: list of tuples
        @param num_of_items: number of items to show
        @param x_label: x axis label
        @param y_label: y axis label
        @param title: title of the chart
        @param file_name: name of the file to save the chart
        """
        data = data[:num_of_items]
        # Create the data frame
        df = pd.DataFrame(data, columns=[x_label, y_label])
        # Create the chart
        df.plot.bar(x=x_label, y=y_label)
        # Set image size
        plt.figure(figsize=(10, 8))
        # Set the title
        plt.title(title)
        # Save the chart
        if file_name is not None:
            plt.savefig(file_name, dpi=300)
        plt.show()
        plt.close()
    
    def create_word_cloud(tweets : list, file : str = None):
        """
        Create a word cloud from a list of tweets
        
        @param tweets: list of tweets
        @param file: name of the file to save the word cloud
        """
        # Merge all tweets into one string
        tweets_text = " ".join([analysis.get_tweet_text(tweet)
                                for tweet in tweets])
        # Create the word cloud
        wordcloud = WordCloud(width=800, height=500, max_font_size=200).generate(tweets_text)
        # Display the word cloud
        plt.figure(figsize=(10, 8), facecolor='k')
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.tight_layout(pad=0)
        # Save the word cloud
        if file is not None:
            plt.savefig(file)
        plt.show()
        plt.close()
        
    def convert_to_huggingface_csv(good_tweets : list, bad_tweets : list, file_name_train : str, file_name_test : str, val_size : float = 0.8):
        """
        Convert a list of tweets to a csv file for use with huggingface
        
        @param good_tweets: list of good tweets
        @param bad_tweets: list of bad tweets
        @param file_name: name of the file to save the csv
        """
        labels = ([1] * len(good_tweets)) + ([0] * len(bad_tweets))
        print("Labels length: ", len(labels))
        print("Good tweets length: ", len(good_tweets))
        print("Bad tweets length: ", len(bad_tweets))
        # Split using stratified sampling
        tweets_train, tweets_test, labels_train, labels_test = train_test_split(good_tweets + bad_tweets, labels, test_size=val_size, stratify=labels)
        print("Tweets train length: ", len(tweets_train))
        print("Labels train length: ", len(labels_train))
        print("Tweets test length: ", len(tweets_test))
        print("Labels test length: ", len(labels_test))
        # Create the data frame
        tweets_train_text = []
        for tweet in tweets_train:
            # Remove all commas and new lines
            tweet_text = analysis.get_tweet_text(tweet).replace(',', '').replace('\n', '')
            tweets_train_text.append(tweet_text)
       
        df = pd.DataFrame(data={"lables": labels_train, "sentence": tweets_train_text})
        df.to_csv(file_name_train, index=False)
        # Do the same for the test data
        tweets_test_text = []
        for tweet in tweets_test:
            # Remove all commas and new lines
            tweet_text = analysis.get_tweet_text(tweet).replace(',', '').replace('\n', '')
            tweets_test_text.append(tweet_text)
        df = pd.DataFrame(data={"lables": labels_test, "sentence": tweets_test_text})
        df.to_csv(file_name_test, index=False)
            
            
            
        
    
            
                
                
