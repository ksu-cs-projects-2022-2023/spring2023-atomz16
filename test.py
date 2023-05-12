import json
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
import string
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def analyze(data):
    post = data['tweet'].lower()
    tokens = word_tokenize(post)

    context_keywords = {'campus', 'program', 'engineering', 'business', 'education', 'class', 'school', 'agriculture', 'alumni', 'ksu', 'kstate', 'k-state'}

    location = data['userLocation']
    if location != "":
        location = location.lower()
        location = location.translate(translator)
        loc_tokens = word_tokenize(location)
        for token in loc_tokens:
            if token == "kennesaw" or token == "ga":
                return False

    for i in range(1, len(tokens)):
        if tokens[i] in context_keywords:
            return True

    return False

translator = str.maketrans("", "", string.punctuation)

with open("kstate_posts.json", "r") as infile:
    dataset1 = json.load(infile)

comments = []
for data in dataset1:
    if analyze(data):
        comments.append(data)

print(len(dataset1))
print(len(comments))

outside_posts = []
for tweet in comments:
    outside = 0
    location = tweet['userLocation']
    if location != "":
        location = location.lower()
        location = location.translate(translator)
        loc_tokens = word_tokenize(location)
        for token in loc_tokens:
            if token != "manhattan" and token != "ks" and token != "mo" and token != "kansas":
                outside = 1
            else:
                outside = 0
    if outside == 1:
        outside_posts.append(tweet)

# Preprocess the comments
def clean_text(text):
    tokens = nltk.word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

analyzer = SentimentIntensityAnalyzer()

results = []
for comment in outside_posts:
    cleaned_text = clean_text(comment['tweet'])
    score = analyzer.polarity_scores(cleaned_text)
    results.append({'score': score, 'votes': comment['likes']})

total_score = 0
for result in results:
    total_score += result['score']['compound']
    

avg_score = total_score / len(results)
print("The average score is - " + str(avg_score))


