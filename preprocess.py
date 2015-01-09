#!/usr/bin/env python
import re

def processStatement(stmt):

	#convert to lower case
	stmt = stmt.lower()
	#remove punctuations and white spaces
	stmt = re.sub('[\s]+', ' ', stmt)
	#trim the stmt
	stmt = stmt.strip('\'"')
	return stmt
 
#Read the statement one by one and process it
fp = open('Desktop/aip.txt', 'r')
line = fp.readline()
 
while line:
		processedStatement = processStatement(line)
		print processedStatement
		line = fp.readline()
#end loop
fp.close()

