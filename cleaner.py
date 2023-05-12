import string
import nltk
from nltk.tokenize import word_tokenize

class Cleaner:

    def __init__(self, counter, subIdSet):
        self.counter = counter
        self.subIdSet = subIdSet

    # Method for looking up keywords and determining if a message is related to Kansas State
    def _analyze(self, msgTokens, subNameTokens, redditMsg):

        # Keywords that identify Kansas State
        context_keywords = {'manhattan', 'aggieville', 'emaw', 'goodnow', 'marlatt', 'wefald', 'derby', 'boyd', 'putnam', 'kstate', 'k-state'}

        # Keywords that don't identify Kasnas State
        bad_context_keywords = {'georgia', 'kennesaw', 'game', 'postgame', 'thread', 'nick'}

        for i in range(len(subNameTokens)):
            if subNameTokens[i] in bad_context_keywords:
                self.subIdSet.add(redditMsg.subID) # Saves submission id's of bad submission names
                return False

        for i in range(len(msgTokens)):
            if msgTokens[i] in bad_context_keywords:
                return False

        for i in range(1, len(msgTokens)):
            if i == 1:
                if msgTokens[0] in context_keywords:
                    return True
            elif msgTokens[i] in context_keywords:
                return True
            elif msgTokens[i - 1] == "kansas" and msgTokens[i] == "state":
                return True

        for i in range(1, len(subNameTokens)):
            if i == 1:
                if subNameTokens[0] in context_keywords:
                    return True
            elif subNameTokens[i] in context_keywords:
                return True
            elif subNameTokens[i - 1] == "kansas" and subNameTokens[i] == "state":
                return True

        return False

    # Method to clean a Reddit message 
    def clean(self, redditMsg):

        # Counts the number of times we have cleaned a redditMsg
        self.counter += 1

        # First check if the submission ID is in the subset of bad submissions
        if redditMsg.subID in self.subIdSet:
            return False

        # Lower all the characters, remove all punctuation, and tokenize the message
        msg = redditMsg.msg
        msg = msg.lower()
        msg = msg.translate(str.maketrans("", "", string.punctuation))
        msgTokens = word_tokenize(msg)

        subName = redditMsg.subName
        subName = subName.lower()
        subName = subName.translate(str.maketrans("", "", string.punctuation))
        subNameTokens = word_tokenize(subName)

        # Analyze for keywords
        if self._analyze(msgTokens, subNameTokens, redditMsg):
            return True
        else:
            self.subIdSet.add(redditMsg.subID)
            return False

    # Method to check after initial cleaning is done
    def reclean(self, redditMsg):

        if redditMsg.subID in self.subIdSet:
            return False
        return True
