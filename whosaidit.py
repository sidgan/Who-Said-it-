#!/usr/bin/env python

# WHO SAID IT?

#Input a sentence
#Which of the three, Arvind Kejriwal, Rahul Gandhi, Narendra Modi 
#is the most likely to say that sentence. 

#siddha ganju, gaura sinha


#import regex
import re
import csv
import pprint
import nltk.classify

#remove repeats in sentence
def replace_repeat(s):
    #if similar characters then delete
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)
#end

#format sentence to make it computer readable/understandable
def format_stmts(stmts):
    # lower case
    stmts = stmts.lower()
    #Remove additional white spaces
    stmts = re.sub('[\s]+', ' ', stmts)
    #trim
    stmts = stmts.strip('\'"')
    return stmts
#end

#Stop Word List
#unigram words that are neutral and hence do not contribute towards statement speaker identification
def get_StopWordList(stopWordListFileName):
    #read the stopwords from the file already supplied with unigrams
    #keep those words in the stopWords array
    stopWords = []
    fp = open(stopWordListFileName, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        stopWords.append(word)
        line = fp.readline()
    fp.close()
    return stopWords
#end

#  get feature vector
def get_feature_vector(stmts, stopWords):
    feature_vector = []
    words = stmts.split()
    for w in words:
        #replace repeats
        w = replace_repeat(w)
        #punctuation will not help to interpret - this is a basic model - punctuation support will be added later
        w = w.strip('\'"?,.')
        #numerical values are neutral - wont help in prediction 
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*[a-zA-Z]+[a-zA-Z0-9]*$", w)
        #ignore if it is a stopWord - neutral words - all can talk about them
        if(w in stopWords or val is None):
            continue
        else:
            feature_vector.append(w.lower())
    return feature_vector
#end

#start extract_features
def extract_features(stmts):
    stmt_words = set(stmts)
    features = {}
    for word in featureList:
        features['contains(%s)' % word] = (word in stmt_words)
    return features
#end


#Read the sentences one by one and process it
inp_statements = csv.reader(open('/home/firenze/Desktop/aip.csv', 'rb'), delimiter=',', quotechar='|')
stopWords = get_StopWordList('/home/firenze/Desktop/stopwords.txt')
count = 0;
featureList = []
statements = []
for row in inp_statements:
    who_said_it = row[0]
    stmts = row[1]
    processed_statements = format_stmts(stmts)
    feature_vector = get_feature_vector(processed_statements, stopWords)
    featureList.extend(feature_vector)
    statements.append((feature_vector, who_said_it));


# Remove featureList duplicates
featureList = list(set(featureList))

# Generate the training set
training_set = nltk.classify.util.apply_features(extract_features, statements)

# Train the Naive Bayes classifier
NBClassifier = nltk.NaiveBayesClassifier.train(training_set)

# Test the classifier
testing123 = 'main hun aam aadmi!'
processed_testing123 = format_stmts(testing123)
who_said_it = NBClassifier.classify(extract_features(get_feature_vector(processed_testing123, stopWords)))
print "Input Statment = %s \nChances are you are listening to: %s \n" % (testing123, who_said_it)

  


