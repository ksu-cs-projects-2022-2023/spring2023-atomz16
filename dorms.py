from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json
import gensim
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import string

# Download the stopwords if necessary
nltk.download('stopwords')
nltk.download('wordnet')

# Preprocess the comments
def clean_text(text):
    tokens = nltk.word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

data = []
with open("kstate_comments.json", "r") as f:
    data = json.load(f)

analyzer = SentimentIntensityAnalyzer()
translator = str.maketrans("", "", string.punctuation)
submission_ids = set()

marlatt = []
goodnow = []
wefald = []
kramer = []
moore = []
west = []
haymaker = []
ford = []
derby = []
boyd = []
vz = []
putnam = []

print("Starting cleaning")
cleaned_comments = []
for comment in data:
    body = comment['body'].lower()
    body = body.translate(translator)
    tokens = word_tokenize(body)

    for i in range(len(tokens)):
        if tokens[i] == "marlatt":
            marlatt.append(comment['body'])
        elif tokens[i] == "goodnow":
            goodnow.append(comment['body'])
        elif tokens[i] == "wefald":
            wefald.append(comment['body'])
        elif tokens[i] == "kramer":
            kramer.append(comment['body'])
        elif tokens[i] == "moore":
            moore.append(comment['body'])
        elif tokens[i] == "west":
            west.append(comment['body'])
        elif tokens[i] == "haymaker":
            haymaker.append(comment['body'])
        elif tokens[i] == "ford":
            ford.append(comment['body'])
        elif tokens[i] == "derby":
            derby.append(comment['body'])
        elif tokens[i] == "boyd":
            boyd.append(comment['body'])
        elif tokens[i] == "zile":
            vz.append(comment['body'])
        elif tokens[i] == "putnam":
            putnam.append(comment['body'])

marlatt_score = 0
score = 0
for comment in marlatt:
    cleaned_text = clean_text(comment)
    score += analyzer.polarity_scores(cleaned_text)['compound']
marlatt_score = score / len(marlatt)

goodnow_score = 0
score = 0
for comment in goodnow:
    cleaned_text = clean_text(comment)
    score += analyzer.polarity_scores(cleaned_text)['compound']
goodnow_score = score / len(goodnow)

wefald_score = 0
score = 0
for comment in wefald:
    cleaned_text = clean_text(comment)
    score += analyzer.polarity_scores(cleaned_text)['compound']
wefald_score = score / len(wefald)

kramer_score = 0
score = 0
for comment in kramer:
    cleaned_text = clean_text(comment)
    score += analyzer.polarity_scores(cleaned_text)['compound']
kramer_score = score / len(kramer)

moore_score = 0
score = 0
for comment in moore:
    cleaned_text = clean_text(comment)
    score += analyzer.polarity_scores(cleaned_text)['compound']
moore_score = score / len(moore)

west_score = 0
score = 0
for comment in west:
    cleaned_text = clean_text(comment)
    score += analyzer.polarity_scores(cleaned_text)['compound']
west_score = score / len(west)

hay_score = 0
score = 0
for comment in haymaker:
    cleaned_text = clean_text(comment)
    score += analyzer.polarity_scores(cleaned_text)['compound']
hay_score = score / len(haymaker)

ford_score = 0
score = 0
for comment in ford:
    cleaned_text = clean_text(comment)
    score += analyzer.polarity_scores(cleaned_text)['compound']
ford_score = score / len(ford)

derby_score = 0
score = 0
for comment in derby:
    cleaned_text = clean_text(comment)
    score += analyzer.polarity_scores(cleaned_text)['compound']
derby_score = score / len(derby)

boyd_score = 0
score = 0
for comment in boyd:
    cleaned_text = clean_text(comment)
    score += analyzer.polarity_scores(cleaned_text)['compound']
boyd_score = score / len(boyd)

vz_score = 0
score = 0
for comment in vz:
    cleaned_text = clean_text(comment)
    score += analyzer.polarity_scores(cleaned_text)['compound']
vz_score = score / len(vz)

putnam_score = 0
score = 0
for comment in putnam:
    cleaned_text = clean_text(comment)
    score += analyzer.polarity_scores(cleaned_text)['compound']
putnam_score = score / len(putnam)

print("Marlatt " + str(marlatt_score))
print("Goodnow " + str(goodnow_score))
print("Wefald " + str(wefald_score))
print("Kramer " + str(kramer_score))
print("Moore " + str(moore_score))
print("West " + str(west_score))
print("Haymaker " + str(hay_score))
print("Ford " + str(ford_score))
print("Derby " + str(derby_score))
print("Boyd " + str(boyd_score))
print("VZ " + str(vz_score))
print("Putnam " + str(putnam_score))