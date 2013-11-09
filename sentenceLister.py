#!/usr/bin/python

import os

def sentenceLister(file):
	'''
	1. Open file
	2. Split text on periods BUT ALSO get the id of article that the sentence came from
	3. Return dict object
			{ 'id': [sents] } where [sents] is a list of sentences from the article.
	'''

