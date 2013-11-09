#!/usr/bin/python

import os
import re
import string
from pprint import pprint
from cPickle import load, dump


# Where the entity's key and value starts
keyStartIndex = 0
valueStartIndex = 0

# String manipulation
mkTrans = string.maketrans("", "")
punc = string.punctuation

def entityLister(filename):
  '''
  1. Opens file
  2. Gets all entities where key is entity's name and value is entity's value
  e.g. 'Location': 'California'
  3. Stores all entities of a particular ID as a dictionary
  3. Gets a final dict object
      { 'id': {entities} } where {entities} is a dictionary of entities
      that belongs to the document with 'id'
  4. Pickles the dict object
  '''
  with open(filename, 'r') as f:
    keyDict = {}
    listOfLines = f.readlines()
    indexFound = False
    lastDocID = 0

    # Loop over all the lines and get the entities
    for line in listOfLines:
      line = line.strip()
      if line.startswith(';;;') or line == '':
        continue # ignore comment line
      elif line.startswith('0'):
        if not indexFound:
          kSI, vSI = detectStartIndex(line)
          indexFound = True

        # Start of a new document
        entities = {}
        notUsedKey, docID = extractLine(line, kSI, vSI)
        keyDict[docID] = entities
        print "Processing document", docID
        lastDocID = docID
      elif coerceToInt(line[0]):
        key, value = extractLine(line, kSI, vSI)
        keyDict[lastDocID][key] = value

  filename = filename[filename.rindex("/"):]
  pickleLocation = "pickle/" + filename + ".pickle"
  print "Pickling into", filename
  with open(pickleLocation, "wb") as f:
    dump(keyDict, f)

def detectStartIndex(line):
  '''
  Detects the start indices of the entity name and value
  and returns them as a tuple
  '''
  keyStartIndex = 0
  valueStartIndex = 0
  keyFound = False
  valueFound = False
  consecutiveWhitespace = 0

  for i in range(len(line)):
    if not keyFound and line[i].isalpha():
      keyStartIndex = i
      keyFound = True
    elif line[i] == ' ' and line[i-1] == ' ':
      consecutiveWhitespace += 1
    elif not valueFound and line[i].isalpha() and\
         consecutiveWhitespace > 5:
      valueStartIndex = i
      valueFound = True
    elif keyFound and valueFound:
      break
  return keyStartIndex, valueStartIndex

def extractLine(line, keyStartIndex, valueStartIndex):
  '''
  Extracts a line and returns a tuple of 
  (entity's name, entity's value) using the given index

  Also does some preprocessing by stripping out all punctuation
  '''
  key = ' '.join(line[keyStartIndex:valueStartIndex].
    translate(mkTrans, punc).strip().split())
  value = ' '.join(line[valueStartIndex:].
    translate(mkTrans, punc).strip().split())
  return key, value

def coerceToInt(char):
  '''
  Returns true if the character can be coerced to int, false otherwise
  '''
  try:
    num = int(char)
    return True
  except ValueError:
    return False

def loadPickle(pickleLocation):
  '''
  Returns the dictionary that was pickled at pickleLocation
  '''
  with open(pickleLocation, "rb") as f:
    return load(f)

if __name__ == '__main__':
  entityLister('data/tst2/key-tst2.v4')
