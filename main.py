#!/usr/bin/python

import os
import requests
import simplejson as sj
import dateutil.parser as dup
#from auth import authenticate 		>>what pip install do I need to run to get this?
from pprint import pprint
from datetime import datetime as dt
#from util import *					>>depends on line 7
from cPickle import load,dump
from preRec import calcPrecRec

cwd = os.getcwd()

# Set up your API key here. Make an auth.py file with a function 
# authenticate() that returns the API key. Don't check auth.py 
# into git :(
#api_key = authenticate()

# Requests URL
interpret_url = "http://napi.maluuba.com/v0/interpret"

def main():
  '''
  highest level: what are we doing?

	1. Use each file to create a masterDictionary where keys are article id's and the values are lists of sentences in that article.
	2. Process the answer key files to create a similar dictionary as step 2, but the values contain the entities of the article
		(we will use a subset of the entities. Q: what data structure for the values of this dict?)
	3. For each article in masterDictionary:
		a. send sentences to be interpreted by Maluuba API
		b. synchronize format of response to compare to entities in answer key.
		c. calculate precision/recall
  '''
  pMD = open(cwd+'/pickle/allInputFiles.pickle','r')
  pKD = open(cwd+ '/pickle/allKeysDict.pickle','r')
  masterDict = load(pMD)
  keyDict = load(pKD)
  pMD.close()
  pKD.close()
  pMLD = open(cwd+'/pickle/maluubaKeysDict.pickle')
  maluubaKeysDict = load(pMLD)
  pMLD.close()

  '''maluubaDict = {}
  for docID in masterDict:
    print "Processing", docID
    sents = masterDict[docID]
    entities = getMaluubaDict(sents)
    maluubaDict[docID] = entities
    print "Finish", docID, "\n"
  pickleStuff(maluubaDict, "maluubaKeysDict")'''

  calcPrecRec(keyDict,maluubaKeysDict)

if __name__ == "__main__":
  main()
