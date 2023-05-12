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

ku_subreddits = []
ku_subreddits.append(reddit.subreddit("UniversityofKansas"))
ku_subreddits.append(reddit.subreddit("jayhawks"))
ku_subreddits.append(reddit.subreddit("Lawrence"))

isu_subreddits = []
isu_subreddits.append(reddit.subreddit("IowaState"))
isu_subreddits.append(reddit.subreddit("iastate"))

wvu_subreddits = []
wvu_subreddits.append(reddit.subreddit("WVU"))

osu_subreddits = []
osu_subreddits.append(reddit.subreddit("OKState"))
osu_subreddits.append(reddit.subreddit("OklahomaState"))

ou_subreddits = []
ou_subreddits.append(reddit.subreddit("sooners"))
ou_subreddits.append(reddit.subreddit("universityofoklahoma"))
ou_subreddits.append(reddit.subreddit("OklahomaSooners"))

texas_subreddits = []
texas_subreddits.append(reddit.subreddit("UTAustin"))

ttu_subreddits = []
ttu_subreddits.append(reddit.subreddit("TexasTech"))

tcu_subreddits = []
tcu_subreddits.append(reddit.subreddit("TCU"))

baylor_subreddits = []
baylor_subreddits.append(reddit.subreddit("baylor"))
baylor_subreddits.append(reddit.subreddit("bayloruniversity"))
"""
comments = []
subreddits_reached = 0
print('Starting KU search')
start_time = time.time()
for subreddit in ku_subreddits:
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

with open("ku_comments.json", "w") as outfile:
    json.dump(comments, outfile, indent=4)

end_time = time.time()
elapsed_time = end_time - start_time
print('Collected ' + str(len(comments)) + ' in' + f"{elapsed_time: .2f}" + ' seconds')

comments = []
subreddits_reached = 0
print('Starting ISU search')
start_time = time.time()
for subreddit in isu_subreddits:
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

with open("isu_comments.json", "w") as outfile:
    json.dump(comments, outfile, indent=4)

end_time = time.time()
elapsed_time = end_time - start_time
print('Collected ' + str(len(comments)) + ' in' + f"{elapsed_time: .2f}" + ' seconds')
"""
comments = []
subreddits_reached = 0
print('Starting WVU search')
start_time = time.time()
for subreddit in wvu_subreddits:
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

with open("wvu_comments.json", "w") as outfile:
    json.dump(comments, outfile, indent=4)

end_time = time.time()
elapsed_time = end_time - start_time
print('Collected ' + str(len(comments)) + ' in' + f"{elapsed_time: .2f}" + ' seconds')

comments = []
subreddits_reached = 0
print('Starting OSU search')
start_time = time.time()
for subreddit in osu_subreddits:
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

with open("osu_comments.json", "w") as outfile:
    json.dump(comments, outfile, indent=4)

end_time = time.time()
elapsed_time = end_time - start_time
print('Collected ' + str(len(comments)) + ' in' + f"{elapsed_time: .2f}" + ' seconds')

comments = []
subreddits_reached = 0
print('Starting OU search')
start_time = time.time()
for subreddit in ou_subreddits:
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

with open("ou_comments.json", "w") as outfile:
    json.dump(comments, outfile, indent=4)

end_time = time.time()
elapsed_time = end_time - start_time
print('Collected ' + str(len(comments)) + ' in' + f"{elapsed_time: .2f}" + ' seconds')

comments = []
subreddits_reached = 0
print('Starting Texas search')
start_time = time.time()
for subreddit in texas_subreddits:
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

with open("texas_comments.json", "w") as outfile:
    json.dump(comments, outfile, indent=4)

end_time = time.time()
elapsed_time = end_time - start_time
print('Collected ' + str(len(comments)) + ' in' + f"{elapsed_time: .2f}" + ' seconds')

comments = []
subreddits_reached = 0
print('Starting TTU search')
start_time = time.time()
for subreddit in ttu_subreddits:
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

with open("ttu_comments.json", "w") as outfile:
    json.dump(comments, outfile, indent=4)

end_time = time.time()
elapsed_time = end_time - start_time
print('Collected ' + str(len(comments)) + ' in' + f"{elapsed_time: .2f}" + ' seconds')

comments = []
subreddits_reached = 0
print('Starting TCU search')
start_time = time.time()
for subreddit in tcu_subreddits:
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

with open("tcu_comments.json", "w") as outfile:
    json.dump(comments, outfile, indent=4)

end_time = time.time()
elapsed_time = end_time - start_time
print('Collected ' + str(len(comments)) + ' in' + f"{elapsed_time: .2f}" + ' seconds')

comments = []
subreddits_reached = 0
print('Starting Baylor search')
start_time = time.time()
for subreddit in baylor_subreddits:
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

with open("baylor_comments.json", "w") as outfile:
    json.dump(comments, outfile, indent=4)

end_time = time.time()
elapsed_time = end_time - start_time
print('Collected ' + str(len(comments)) + ' in' + f"{elapsed_time: .2f}" + ' seconds')