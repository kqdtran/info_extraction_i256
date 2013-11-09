import requests
import simplejson as sj
from auth import authenticate


# Set up your API key here. Make an auth.py file with a function 
# authenticate() that returns the API key. Don't check auth.py 
# into git :(
api_key = authenticate()

# Requests URL
interpret_url = "http://napi.maluuba.com/v0/interpret"
normalize_url = "http://napi.maluuba.com/v0/normalize"

def interpret(sentence="I love Natural Language Processing"):
  params = {"phrase": sentence, "apikey": api_key}
  req = requests.get(interpret_url, params=params)
  result = sj.loads(req.content)
  print result

if __name__ == "__main__":
  interpret()
