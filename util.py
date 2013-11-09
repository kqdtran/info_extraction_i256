import os
from cPickle import dump, load

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
  for sent in sentList:
    pass

if __name__ == "__main__":
  allKeyDict = getAllKeyFiles()
  pickleStuff(allKeyDict)
