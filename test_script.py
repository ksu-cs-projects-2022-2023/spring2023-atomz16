import praw
import time
import threading
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
    for i in range(0, len(tokens)-1):
        if tokens[i] == 'kansas' and tokens[i+1] == 'state' or tokens[i] == 'ksu':
            return True
    return False

comments_collected = 0
subreddits_reached = 0
print('Starting seach')
start_time = time.time()
try:
    for subreddit in reddit.subreddits.search(query='College'):
        if subreddit.over18 != True:
            subreddits_reached+=1
            print('Subreddit #' + str(subreddits_reached))
            for submission in subreddit.search(query='Kansas State', time_filter='year'):
                submission.comments.replace_more()
                for comment in submission.comments.list():
                    if analyze(comment.body) == True:
                        comments_collected += 1
except Forbidden:
    print('End of search')
end_time = time.time()
elapsed_time = end_time - start_time
print('Total comments collected = ' + str(comments_collected) + ' in ' + f"{elapsed_time: .2f}" + ' seconds')