#!/usr/bin/python

import os
import requests
import simplejson as sj
import dateutil.parser as dup
from auth import authenticate
from pprint import pprint
from datetime import datetime as dt


# Set up your API key here. Make an auth.py file with a function 
# authenticate() that returns the API key. Don't check auth.py 
# into git :(
api_key = authenticate()

# Requests URL
interpret_url = "http://napi.maluuba.com/v0/interpret"
normalize_url = "http://napi.maluuba.com/v0/normalize"

def main():
  '''
  highest level: what are we doing?

	2. Use each file to create a masterDictionary where keys are article id's and the values are lists of sentences in that article.
	3. Process the answer key files to create a similar dictionary as step 2, but the values contain the entities of the article
		(we will use a subset of the entities. Q: what data structure for the values of this dict?)
	4. For each article in masterDictionary:
		4a. send sentences to be interpreted by Maluuba API
		4b. synchronize format of response to compare to entities in answer key.
		4c. calculate precision/recall
  '''
  #masterDict = getAllInputFiles()
  #keyDict = getAllKeyFiles()

if __name__ == "__main__":
  main()
