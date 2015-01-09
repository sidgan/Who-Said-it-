#!/usr/bin/env python

import preprocess
import getFeatureVector
import re
import csv



#start extract_features
def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in featureList:
        features['contains(%s)' % word] = (word in tweet_words)
    return features
#end


inpStatements = csv.reader(open('Desktop/aip.csv', 'rb'), delimiter=',', quotechar='|')
stmts = []
featureList = []
for row in inpStatements:
	politician = row[0]
	statement = row[1]
	processedStatement = preprocess.processStatement(statement)
	feature_vector = getFeatureVector.get_Feature_Vector(processedStatement, getFeatureVector.stopWords)
	stmts.append((feature_vector, politician));
#end loop

featureList = list(set(featureList))

# Generate the training set
training_set = nltk.classify.util.apply_features(extract_features, stmts)

# Train the Naive Bayes classifier
NBClassifier = nltk.NaiveBayesClassifier.train(training_set)

# Test the classifier
testTweet = 'Congrats @ravikiranj, i heard you wrote a new tech post on sentiment analysis'
processedTestTweet = processTweet(testTweet)
sentiment = NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet, stopWords)))
print "testTweet = %s, sentiment = %s\n" % (testTweet, sentiment)


