import os
import requests
from cPickle import dump, load
from auth import authenticate


# Set up your API key here. Make an auth.py file with a function 
# authenticate() that returns the API key. Don't check auth.py 
# into git :(
api_key = authenticate()

# Requests URL
interpret_url = "http://napi.maluuba.com/v0/interpret"

def getAllInputFiles():
  '''
  Gets all input text files, which is a dictionary of 
  {id: list of sentences}
  '''
  with open("pickle/allInputFiles.pickle", "rb") as f:
    masterDict = load(f)
    return masterDict

def getAllKeyFiles():
  '''
  Gets all the key files, and return one big dictionary
  consists of all four test files
  '''
  allKeyDict = {}
  allKeyFiles = os.walk("pickle/")
  for tup in allKeyFiles:
    for filename in tup[2]:
      if filename.startswith('k'):
        with open("pickle/" + filename, "rb") as f:
          keyDict = load(f)
          allKeyDict.update(keyDict)
  return allKeyDict

def pickleStuff(stuff):
  '''
  Pickles keys dictionary for later use
  '''
  with open("pickle/allKeysDict.pickle", "wb") as f:
    dump(stuff, f)

def loadPickle(location):
  '''
  Loads the pickle at the given location
  '''
  with open(location, "rb") as f:
    return load(f)

def getMaluubaDict(sentList):
  '''
  Input would be a list of sentences, and the key that points to
  this sentence would be the ID of the article
  '''
  allEntities = {}
  for sent in sentList:
    entities = interpret(sent)
    for key in entities:
      val = entities[key]
      if key in allEntities:
        allEntities[key].append(val) # append to existing key
      else:
        allEntities[key] = val
  return allEntities
    
def interpret(sentence="I love Natural Language Processing"):
  '''
  Interprets a sentence and get all the recognized entities 
  using the Maluuba API
  '''
  params = {"phrase": sentence, "apikey": api_key}
  req = requests.get(interpret_url, params=params)
  return sj.loads(req.content)['entities']

if __name__ == "__main__":
  allKeyDict = getAllKeyFiles()
  pickleStuff(allKeyDict)
