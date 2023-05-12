import json
from collections import Counter

class EngagementAnalyzer:

    def __init__(self):
        pass

    def analyze(self, data):

        user_input = input("Total Network(0), Total Active Users(1), Avg Active Users(2):\nSelection: ")

        if user_input == "0":
            self.networkAnalysis(data)

        if user_input == "1":
            self.activeUsers(data)

        if user_input == "2":
            self.averageActiveUsers(data)

    # Method for building a network of each individual in a dataset
    def networkAnalysis(self, data):
        network = set()
        for redditMsg in data:
            network.add(redditMsg.author)

        print("Total people in the network on this file is " + str(len(network)))
        return len(network)

    # Method for getting active users in a dataset
    def activeUsers(self, data):
        users = []
        for redditMsg in data:
            users.append(redditMsg.author)

        counter = Counter(users)

        active_users = []
        for author, count in counter.most_common():
            if count >= 10: # Number can be changed as fit
                active_users.append(author)

        print("The total active users for this file is " + str(len(active_users)))
        return len(active_users)

    # Method for getting the ratio of active users to total users in the dataset
    def averageActiveUsers(self, data):
        total_users = self.networkAnalysis(data)
        active_users = self.activeUsers(data)
        print("The average active users in this file is " + "{:.2f}".format(active_users/total_users*100))
