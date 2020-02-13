import re


MAX_TWEETS = 15
TWEET_LIMIT = 140 - len(str(MAX_TWEETS)) - len("/")
MAX_LEN = TWEET_LIMIT * MAX_TWEETS
MIN_LEN = 1


class Tweetsplit(object):

    def __init__(self, text):
        self.text = re.sub('\s+', ' ', text.strip())

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.validate_text(value)
        self.__text = value

    def validate_text(self, text):
        def validate_limit(strings):
            for string in strings:
                if len(string) > TWEET_LIMIT:
                    raise ValueError("the strings exceds TWEET_LIMIT")

        if len(text) > MAX_LEN:
            raise ValueError("text lenght exceeds MAX_LEN")
        if len(text) < MIN_LEN:
            raise ValueError("text lenght must be greather than MIN_LEN")
        try:
            validate_limit(text.split("."))
        except ValueError:
            raise ValueError(
                "the text must have a dot delimiter(.) "
                "and the each parts shouldn't exceeds %i chars" % TWEET_LIMIT
                )

    def chunk(self, strings, tweets=None, index=0):
        """
            get strings and chunk into parts for retrieve posts
        """
        tweet = ""
        if not tweets:
            tweets = []

        while len(tweet) < TWEET_LIMIT:
            tweet += strings[index].strip()
            tweet += "."
            index += 1
            if index >= len(strings):
                break
            if len(tweet + strings[index].strip()) > TWEET_LIMIT:
                break

        tweets.append(tweet)
        if index >= len(strings):
            return tweets

        return self.chunk(strings=strings, tweets=tweets, index=index)

    def retrieve_posts(self):
        """
            retrieve posts from given text argument on constructor
        """
        tweets = self.chunk(strings=self.text.split("."))
        posts = []
        for i, t in enumerate(tweets):
            posts.append("%i/%s" % (i+1, t))

        return posts
