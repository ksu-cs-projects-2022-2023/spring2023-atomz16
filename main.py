from redditMsg import RedditMsg
from cleaner import Cleaner
from topic_analysis import TopicAnalyzer
from sentiment_analysis import SentimentAnalyzer
from engagement_analysis import EngagementAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import json
import praw
import prawcore.exceptions

def main():

    user_input = input("Please select a number: \n0 - new search\n1 - cleaning\n2 - sentiment\n3 - topic\n4 - engagement\nSelection: ")

    # Conduct a new search
    if user_input == '0':
        filename = input("Please enter a filename for the data to be saved\nExample: reddit_comments.json\nFilename: ")
        start_reddit_search(create_reddit_instance(), filename)

    # Conduct cleaning on file
    if user_input == '1':

        filename = input("Please enter a file to be analyzed (JSON Only)\nExample: reddit_comments.json\nFilename: ")

        cleaner = Cleaner(0, set())
        data = openJson(filename)
        comments = clean_comments(cleaner, data)

        print("Total comments collected - " + str(cleaner.counter))
        print("Total comments after cleaning - " + str(len(comments)))

        comments = [redditMsg_to_json(redditMsg) for redditMsg in comments]

        """
        merge_data = []
        with open("kstate_cleaned_comments", "r") as infile:
            merge_data = json.load(infile)
            infile.close()

        merge_data.append(comments)

        """

        # Change the name of the file for the new cleaned comment data
        with open("kstate_cleaned_comments", "w") as outfile:
            json.dump(comments, outfile, indent=4)
            outfile.close()

    # Conduct sentiment analysis
    if user_input == '2':

        filename = input("Please enter a file to be analyzed (JSON Only)\nExample: reddit_comments.json\nFilename: ")

        sentiment_analyzer = SentimentAnalyzer(SentimentIntensityAnalyzer())
        data = openJson(filename)

        comments = []
        for comment in data:
            comments.append(json_to_redditmsg(comment))
        
        sentiment_analyzer.analyze(comments)
    
    # Conduct topic analysis
    if user_input == '3':

        filename = input("Please enter a file to be analyzed (JSON Only)\nExample: reddit_comments.json\nFilename: ")
        
        topic_analyzer = TopicAnalyzer()

        data = openJson(filename)

        comments = []
        for comment in data:
            comments.append(comment['body'])

        topic_analyzer.getTopics(comments)

    # Conduct engagement analysis
    if user_input == '4':

        filename = input("Please enter a file to be analyzed (JSON Only)\nExample: reddit_comments.json\nFilename: ")

        engagement_analyzer = EngagementAnalyzer()

        data = openJson(filename)

        comments = []
        for comment in data:
            comments.append(json_to_redditmsg(comment))

        engagement_analyzer.analyze(comments)


def json_to_redditmsg(jsonLibrary):

    msgID = 0
    msg = jsonLibrary['body']
    subID = jsonLibrary['submission_id']
    subName = jsonLibrary['submission_title']
    author = jsonLibrary['author']
    score = jsonLibrary['score']
    created = jsonLibrary['created_utc']

    return RedditMsg(msgID, msg, subID, subName, author, score, created)

def redditMsg_to_json(redditMsg):
    json_dict = {
        "body": redditMsg.msg,
        "submission_id": redditMsg.subID,
        "submission_title": redditMsg.subName,
        "auhtor": redditMsg.author,
        "score": redditMsg.score,
        "created_utc": redditMsg.created
    }
    return json_dict

def create_reddit_instance():

    # create a Reddit instance with your app's client ID and secret key
    reddit = praw.Reddit(client_id='bo_GpmWm5LwHuu0WzqFBgA',
                         client_secret='itpdoMbtNW6x5CxZSsoRuihRcXBQ4A',
                         user_agent='atomz19')

    return reddit

def start_reddit_search(reddit, filename):
    comments = []

    with open(filename, 'a') as file:
        file.write('[\n')
        try:
            count = 0
            for subreddit in reddit.subreddits.search(query='College'): # Edit subreddit query words
                if subreddit.over18 != True:
                    count += 1
                    print("Subreddit #" + str(count))
                    for submission in subreddit.search(query='ksu OR k-state OR KSU OR K-State'): # Edit submission query words here
                        submission.comments.replace_more()
                        for comment in submission.comments.list():
                            comment_data = {
                                "author": str(comment.author),
                                "created_utc": comment.created_utc,
                                "body": comment.body,
                                "submission_title": comment.submission.title,
                                "submission_id": comment.submission.id,
                                "score": comment.score,
                                "comment_id": comment.id,
                                }

                            json.dump(comment_data, file, indent=4)
                            file.write(',\n')

            file.write(']')     
        except (prawcore.exceptions.PrawcoreException,) as e:
            print(f"An error occurred: {e}")
            file.write(']')
            file.close()

def clean_comments(cleaner, data):
    cleanedComments = []
    for comment in data:
        redditMessage = json_to_redditmsg(comment)
        if cleaner.clean(redditMessage):
            cleanedComments.append(redditMessage)

    return cleanedComments

def openJson(filename):
    data = []
    with open(filename, 'r') as infile:
        data = json.load(infile)
        infile.close()

    return data

if __name__ == "__main__":
    main()