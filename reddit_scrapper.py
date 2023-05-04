import praw
import time
import json
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from prawcore.exceptions import Forbidden

# create a Reddit instance with your app's client ID and secret key
reddit = praw.Reddit(client_id='bo_GpmWm5LwHuu0WzqFBgA',
                     client_secret='itpdoMbtNW6x5CxZSsoRuihRcXBQ4A',
                     user_agent='atomz19')

def analyze(post):
    post = post.lower()
    tokens = word_tokenize(post)

    context_keywords = {'k-state', 'ksu', 'kstate'}

    for i in range(1, len(tokens)):
        if i == 1:
            if tokens[0] in context_keywords:
                return True
        elif tokens[i] in context_keywords:
            return True
        elif tokens[i-1] == "kansas" and tokens[i] == "state":
            return True

    return False

comments = []
subreddits_reached = 0
print('Starting seach')
start_time = time.time()
for submission in reddit.subreddit('College').new(limit=None):
        submission.comments.replace_more()
        for comment in submission.comments.list():
                if analyze(comment.body) == True:
                        comments.append({
                        "author": str(comment.author),
                        "created_utc": comment.created_utc,
                        "body": comment.body,
                        "submission_title": comment.submission.title,
                        "submission_id": comment.submission.id,
                        "score": comment.score,
                        "comment_id": comment.id,
                        })

with open("college_comments.json", "w") as outfile:
    json.dump(comments, outfile, indent=4)

end_time = time.time()
elapsed_time = end_time - start_time
print('Collected ' + str(len(comments)) + ' in' + f"{elapsed_time: .2f}" + ' seconds')



