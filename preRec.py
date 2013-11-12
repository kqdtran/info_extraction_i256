#!/usr/bin/python

from __future__ import division

def calcPrecRec(keyDict, maluDict):
	'''
	Calculates the precision and recall based on the key Dictionary 
	in the corpus and the Maluuba dict, which is converted from the 
	JSON result after sending a request using the Maluuba API
	'''
	articles = maluDict.keys()
	rel = 0
	ret = 0
	relret = 0
	for a in articles:
		maluEnts = maluDict[a]
		keyEnts = keyDict[a]
		keyLoc = set(keyEnts['INCIDENT LOCATION'].lower().split())
		try:
			#Check whether Maluuba found any locations
			maluLoc = set(maluEnts['location'][0].split())
			#Now check whether key has locations
			if len(keyLoc) > 0:
				inter = maluLoc.intersection(keyLoc)
				#Check for intersection
				if len(inter) > 0:
					relret += 1
				else:
					#No intersection, add to retrieved entity count
					ret += 1
			else:
				ret += 1
				#Maluuba found locations not in key, add to entity count 
		except KeyError:
			if len(keyLoc) > 0:
				rel += 1
				#Maluuba didn't find locations it should have, add to relevant entity count
			else:
				pass
	pr = relret/ret
	re = relret/rel
	print('Precision: '+str(pr))
	print('Recall: '+str(re))
	return (pr,re)
