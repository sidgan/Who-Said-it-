#!/usr/bin/env python
#initialize stopWords
stopWords = []

import preprocess 
import re

#start getStopWordList
def getStopWordList(stopWordListFileName):
	#read the stopwords file and build a list
	stopWords = []
	stopWords.append('AT_USER')
	stopWords.append('URL')
 
	fp = open(stopWordListFileName, 'r')
	line = fp.readline()
	while line:
		word = line.strip()
		stopWords.append(word)
		line = fp.readline()
	fp.close()
	return stopWords
#end
 
#start getfeatureVector
def get_Feature_Vector(stmt,stopWords):
	feature_vector = []
	#break statement into words
	words = stmt.split()
	for w in words:
		#remove punctuation
		w = w.strip('\'"?,.')
		#check if the word starts with an alphabet
		val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
		#ignore if it is a stop word
		if(w in stopWords or val is None):
			continue
		else:
			feature_vector.append(w.lower())
	return feature_vector
#end
 
 
#Read the statements one by one and process them
fp = open('Desktop/aip.txt', 'r')
line = fp.readline()
 
st = open('Desktop/stopwords.txt', 'r')
stopWords = getStopWordList('Desktop/stopwords.txt')
 
while line:
	processedStatement = preprocess.processStatement(line)
	feature_vector = get_Feature_Vector(processedStatement, stopWords)
	print feature_vector
	line = fp.readline()
#end loop
fp.close()
