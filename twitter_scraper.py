import praw
import datetime
import threading

# create a Reddit instance with your app's client ID and secret key
reddit = praw.Reddit(client_id='bo_GpmWm5LwHuu0WzqFBgA',
                     client_secret='itpdoMbtNW6x5CxZSsoRuihRcXBQ4A',
                     user_agent='atomz19')

# define the subreddit you want to scrape
subreddit = reddit.subreddit('college')

comments = []
comments_collected = 0
def collect_comments(comment):
        global comments_collected
        if comment not in comments:
                comments.append(comment)
                comments_collected += 1
                print(str(comments_collected) + " Comment Collected")

def reddit_stream():
        for comment in subreddit.stream.comments():
                collect_comments(comment)

thread = threading.Thread(target=reddit_stream)
thread.start()

stop_thread = input("To stop collecting comments press Enter")
thread.join(timeout=1)
print("You collected " + str(comments_collected) + " comments")

for comment in comments:
        time = datetime.datetime.fromtimestamp(comment.created_utc)
        print("-----Posted At " + time.strftime("%Y-%m-%d %H:%M:%S") + "------")
        print(comment.body)





