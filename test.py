#!/usr/bin/python

import requests
import dateutil.parser as dup
import simplejson as sj
from auth import authenticate
from datetime import datetime as dt


# Set up your API key here. Make an auth.py file with a function 
# authenticate() that returns the API key. Don't check auth.py 
# into git :(
api_key = authenticate()

# Requests URL
interpret_url = "http://napi.maluuba.com/v0/interpret"
normalize_url = "http://napi.maluuba.com/v0/normalize"

text = """SPANISH FOREIGN MINISTER LUIS YANEZ [AS HEARD] REPORTED TODAY THAT
SPAIN HAS SUSPENDED AID TO THE SALVADORAN GOVERNMENT. 
POLICE SOURCES HAVE REPORTED THAT THE EXPLOSION CAUSED SERIOUS
DAMAGE TO THE SALVADORAN EMBASSY BUILDING AND TO NEARBY STRUCTURES IN
THE ELEGANT PROVIDENCIA NEIGHORHOOD IN EASTERN SANTIAGO.
AND I'M FROM CHICAGO AND I LIKE THE CHICAGO BULLS. AND KHOA IS FROM VIETNAM. WE GO TO BERKELEY AND WE ARE TAKING A CLASS
TOGETHER. AND WE LIVE NEAR SAN FRANCISCO. AND THE GOLDEN GATE BRIDGE IS NEARBY"""

def interpret(sentence="I love Natural Language Processing"):
  params = {"phrase": sentence, "apikey": api_key}
  req = requests.get(interpret_url, params=params)
  result = sj.loads(req.content)
  print result

if __name__ == "__main__":
  text = text.lower().strip()
  #print text
  interpret(text)
