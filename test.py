import praw
import time
import json
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from prawcore.exceptions import Forbidden
from itertools import islice

# create a Reddit instance with your app's client ID and secret key
reddit = praw.Reddit(client_id='bo_GpmWm5LwHuu0WzqFBgA',
                     client_secret='itpdoMbtNW6x5CxZSsoRuihRcXBQ4A',
                     user_agent='atomz19')

def analyze(post):
    post = post.lower()
    tokens = word_tokenize(post)

    context_keywords = {'k-state', 'ksu', 'kstate', 'campus', 'student', 'professor', 'course', 'degree', 'education', 'aggieville', 'teacher', 'alumni', 'academic',
                            'academics', 'students', 'athletics', 'program', 'engineering', 'business', 'arts'}

    for i in range(len(tokens)):
        if tokens[i] in context_keywords:
            return True

    return False

kstate_subreddits = []
kstate_subreddits.append(reddit.subreddit("KState"))
kstate_subreddits.append(reddit.subreddit("KansasState"))
kstate_subreddits.append(reddit.subreddit("KStateWildcats"))
kstate_subreddits.append(reddit.subreddit("WabashCannonball"))
comments = []
subreddits_reached = 0
print('Starting seach')
start_time = time.time()
for subreddit in kstate_subreddits:
    for submission in subreddit.new(limit=None):
        submission.comments.replace_more()
        for comment in submission.comments.list():
            comments.append({
                "author": str(comment.author),
                "created_utc": comment.created_utc,
                "body": comment.body,
                "submission_title": comment.submission.title,
                "submission_id": comment.submission.id,
                "score": comment.score,
                "comment_id": comment.id,
            })

with open("kstate_comments.json", "w") as outfile:
    json.dump(comments, outfile, indent=4)

end_time = time.time()
elapsed_time = end_time - start_time
print('Collected ' + str(len(comments)) + ' in' + f"{elapsed_time: .2f}" + ' seconds')