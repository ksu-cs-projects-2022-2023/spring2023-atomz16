import json
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import GridSearchCV
from gensim.corpora import Dictionary
from gensim.models import LdaModel
from collections import Counter

nltk.download('stopwords')
nltk.download('wordnet')

def clean_text(text):
    tokens = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    tokens = [word for word in tokens if len(word) >= 3]
    tokens = [word for word in tokens if word != "http" and word != "n't"]
    return tokens

def clean_tokens_text(text):
    tokens = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    tokens = [word for word in tokens if len(word) >= 3]
    tokens = [word for word in tokens if word != "http" and word != "n't"]
    return tokens

training_data = []
with open("negative_comments.json", "r") as infile:
    training_data = json.load(infile)

columns = ['author', 'created', 'body', 'title', 'id', 'score', 'post_id']

df = pd.DataFrame(training_data, columns=columns)

print(df.head())

df['tokens'] = df['body'].apply(clean_text)

dictionary = Dictionary(df['tokens'])

# Filter out words that occur less than 20 times and keep the top 10000 words
dictionary.filter_extremes(no_below=20, no_above=0.5, keep_n=10000)

# Create a bag-of-words representation of the documents
corpus = [dictionary.doc2bow(text) for text in df['tokens']]

num_topics = 10  # Choose the number of topics you want to discover
random_state = 42

lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, random_state=random_state)

for idx, topic in lda_model.print_topics(-1):
    print(f"Topic: {idx} \nWords: {topic}\n")

def get_most_probable_topic(text, lda_model, dictionary):
    tokens = clean_tokens_text(text)
    bow = dictionary.doc2bow(tokens)
    topic_distribution = lda_model.get_document_topics(bow)
    most_probable_topic = sorted(topic_distribution, key=lambda x: x[1], reverse=True)[0][0]
    return most_probable_topic

topics = []
for post in df['body']:
    most_probable_topic = get_most_probable_topic(post, lda_model, dictionary)
    topics.append(most_probable_topic)

counter = Counter(topics)

most_common = counter.most_common(3)

print(most_common)