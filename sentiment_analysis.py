import json
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class SentimentAnalyzer:

    def __init__(self, analyzer):
        self.analyzer = analyzer

    # Preprocess the comments
    def clean_text(self, text):
        tokens = nltk.word_tokenize(text)
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(word) for word in tokens]
        return ' '.join(tokens)

    # Method for splitting the file into positive and negative comments
    def splitSentiment(self, data):
        positive = []
        negative = []
        for comment in data:
            cleaned_text = self.clean_text(comment.msg)
            score = self.analyzer.polarity_scores(cleaned_text)
            if score['compound'] > 0.05:
                positive.append(comment)
            elif score['compound'] < -0.05:
                negative.append(comment)

        # Change file name here for where positive comments are to be saved
        print(len(positive))
        with open('positive_comments.json', "w") as outfile:
            json.dump(positive, outfile, indent=4)
            outfile.close()

        # Change file name here for where negative comments are to be saved
        print(len(negative))
        with open('negative_comments.json', "w") as outfile:
            json.dump(negative, outfile, indent=4)
            outfile.close()

    # Method for getting the average sentiment for a file
    def getAverageScore(self, data):
        total_score = 0.0
        for comment in data:
            cleaned_text = self.clean_text(comment.msg)
            total_score += self.analyzer.polarity_scores(cleaned_text)['compound']
        
        print("The average sentiment for this file is " + str(total_score/len(data)))


    def analyze(self, data):

        user_input = input("Average sentiment score for file (0) or split file into positive and negative(1): ")
        if user_input == "0":
            self.getAverageScore(data)
        if user_input == "1":
            self.splitSentiment(data)

