#!/usr/bin/python

import os
from cPickle import load,dump

def sentenceLister(inputList):
	'''
	1. Open file
	2. Split text on periods BUT ALSO get the id of article that the sentence came from
	3. Return dict object
			{ 'id': [sents] } where [sents] is a list of sentences from the article.
	'''
	masterDict = {}
	for j in range(len(inputList)):
		f = inputList[j]
		ID_PREFIX = str.upper(f[-9:])
		fo = open(f,'r')
		lines = fo.readlines()		
		articleLines = []
		linesLen = len(lines)
		for i in range(linesLen-1,0,-1):
			l = lines[i]
			newArt = False			
			if l[0:9] == ID_PREFIX:
				newArt = True
				articleText = ' '.join(articleLines)
				sents = articleText.split('.')
				ID = l.strip()	
				masterDict[ID] = sents
				articleLines = []	
			if newArt == False:
				articleLines.insert(0,l.strip())
	fo.close()
	return(masterDict)


def main():
	cwd = os.getcwd()
	inputList = [cwd+'/data/tst1/tst1-muc3',cwd+'/data/tst2/tst2-muc4',cwd+'/data/tst3/tst3-muc4',cwd+'/data/tst4/tst4-muc4']
	masterDict = sentenceLister(inputList)
	outName = cwd+'/allInputFiles.pk1'
	outFile = open(outName,'wb')
	dump(masterDict,outFile)
	outFile.close()

main()


