import json
import nltk
import praw
import string
nltk.download('punkt')
from nltk.tokenize import word_tokenize

reddit = praw.Reddit(client_id='bo_GpmWm5LwHuu0WzqFBgA',
                     client_secret='itpdoMbtNW6x5CxZSsoRuihRcXBQ4A',
                     user_agent='atomz19')

def kstate_analyzer(comment):
    title = comment['submission_title'].lower()
    title = title.translate(translator)
    tokens = word_tokenize(title)

    context_keywords = {'kansas', 'manhattan', 'aggieville', 'kc', 'emaw', 'goodnow', 'marlatt', 'wefald', 'derby', 'wildcats', 'wildcat'}

    for i in range(len(tokens)):
        if tokens[i] in context_keywords:
            return (True, comment)

    if kennesaw_analyzer(comment) == False:
        return (False, comment)
    else:
        return (True, comment)

def kennesaw_analyzer(comment):
    title = comment['submission_title'].lower()
    title = title.translate(translator)
    tokens = word_tokenize(title)

    context_keywords = {'kennesaw', 'georgia', 'msu', 'michigan', 'washington', 'isu', 'iowa'}

    for i in range(len(tokens)):
        if tokens[i] in context_keywords:
            return False

    return True

def analyzer(comment):
    body = comment['body'].lower()
    body = body.translate(translator)
    tokens = word_tokenize(body)

    context_keywords = {'kansas', 'manhattan', 'aggieville', 'kc', 'emaw', 'goodnow', 'marlatt', 'wefald', 'derby', 'wildcats', 'wildcat'}
    bad_context_keywords = {'kennesaw', 'georgia', 'msu', 'michigan', 'washington', 'isu', 'iowa'}

    if comment['submission_id'] not in submission_ids:
        for i in range(len(tokens)):
            if tokens[i] in context_keywords:
                return True
            elif tokens[i] in bad_context_keywords:
                if comment['submission_id'] not in submission_ids:
                    submission_ids.add(comment['submission_id'])
                return False

        return_tuple = kstate_analyzer(comment)

        if return_tuple[0] == True:
            return True
        else:
            submission_id = return_tuple[1]['submission_id']
            if submission_id not in submission_ids:
                submission_ids.add(submission_id)
            return False
    else:
        return False

data = []
with open("reddit_comments.json", "r") as f:
    data = json.load(f)

translator = str.maketrans("", "", string.punctuation)
submission_ids = set()

print("Starting cleaning")
cleaned_comments = []
for comment in data[]:
    if analyzer(comment):
        cleaned_comments.append(comment)

recleaned_comments = []
for comment in cleaned_comments:
    if comment['submission_id'] not in submission_ids:
        recleaned_comments.append(comment)

with open("training_data.json", "w") as outfile:
    json.dump(recleaned_comments, outfile, indent=4)

print("Total comments collected after cleaning: " + str(len(recleaned_comments)))
