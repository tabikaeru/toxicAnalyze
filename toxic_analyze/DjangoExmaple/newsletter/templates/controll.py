from newsletter.Toxic.readingToxic import checkingToxic
from newsletter.tweetGet.getTweet import getTweets
from newsletter.tweetGet.makingGraph import makingGraph

import numpy as np
def controllerAnalyzeText(checkText):
    analyzeResults = checkingToxic(checkText)
    # makingGraph
    makingGraph(analyzeResults)

    return analyzeResults

def controllerUserAnalyze(userName):
    analyzeResults = []
    userTweets = getTweets(userName)
    for line in userTweets:
        analyzeResults.append(checkingToxic(line))
    analyzeResults = np.array(analyzeResults)
    analyzeResults = np.mean(analyzeResults, axis=0)

    #makingGraph
    makingGraph(analyzeResults)

    return analyzeResults


