import json
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import numpy as np
import matplotlib.pyplot as plt

class TopicAnalyzer:

    def __init__(self):
        pass

    # Method for cleaning the text
    def clean_text(self, text):
        tokens = nltk.word_tokenize(text)
        stop_words = set(stopwords.words('english'))
        tokens = [word for word in tokens if word not in stop_words]
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(word) for word in tokens]
        tokens = [word for word in tokens if len(word) >= 3]
        frequent_words = {'http', 'www', 'com', 'reddit', 'org', 'the', 'get'}
        tokens = [word for word in tokens if word not in frequent_words]
        return ' '.join(tokens)

    # Method for plotting the results
    def plot_top_words(self, model, feature_names, n_top_words, title):
        fig, axes = plt.subplots(2, 5, figsize=(30, 15), sharex=True)
        axes = axes.flatten()
        for topic_idx, topic in enumerate(model.components_):
            top_features_ind = topic.argsort()[: -n_top_words - 1 : -1]
            top_features = [feature_names[i] for i in top_features_ind]
            weights = topic[top_features_ind]

            ax = axes[topic_idx]
            ax.barh(top_features, weights, height=0.7)
            ax.set_title(f"Topic {topic_idx +1}", fontdict={"fontsize": 30})
            ax.invert_yaxis()
            ax.tick_params(axis="both", which="major", labelsize=20)
            for i in "top right left".split():
                ax.spines[i].set_visible(False)
            fig.suptitle(title, fontsize=40)

        plt.subplots_adjust(top=0.90, bottom=0.05, wspace=0.90, hspace=0.3)
        plt.show()

    # Method for getting the topics from a dataset
    def getTopics(self, comments):

        cleaned_comments_tokens = []
        for comment in comments:
            cleaned_comments_tokens.append(self.clean_text(comment))

        tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2)
        tf = tf_vectorizer.fit_transform(cleaned_comments_tokens)

        lda_model = LatentDirichletAllocation(random_state=3)
        lda_model.fit(tf)

        tf_feature_names = tf_vectorizer.get_feature_names_out()
        self.plot_top_words(lda_model, tf_feature_names, 10, "Topics in LDA model")