from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json
import gensim
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download the stopwords if necessary
nltk.download('stopwords')
nltk.download('wordnet')

# Preprocess the comments
def clean_text(text):
    tokens = nltk.word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

analyzer = SentimentIntensityAnalyzer()

with open('kstate_comments.json', "r") as f:
    data = json.load(f)

positive = []
negative = []
for comment in data:
    cleaned_text = clean_text(comment['body'])
    score = analyzer.polarity_scores(cleaned_text)
    if score['compound'] > 0.05:
        positive.append(comment)
    elif score['compound'] < -0.05:
        negative.append(comment)

print(len(positive))
with open('positive_comments.json', "w") as outfile:
    json.dump(positive, outfile, indent=4)

print(len(negative))
with open('negative_comments.json', "w") as outfile2:
    json.dump(negative, outfile2, indent=4)
