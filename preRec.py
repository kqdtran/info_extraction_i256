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
		#print('')
		#print('Article ID: '+a)
		maluEnts = maluDict[a]
		keyEnts = keyDict[a]
		keyLoc = set(keyEnts['INCIDENT LOCATION'].lower().split())
		#print('Answer Key Locations: '+str(keyLoc))
		try:
			maluLoc = set(maluEnts['location'][0].split())
			#Maluuba found something! But did the key?
			if len(keyLoc) > 0:
				#print('Maluuba API Results: '+str(maluLoc))
				inter = maluLoc.intersection(keyLoc)
				#print('Intersection: '+str(inter))
				if len(inter) > 0:
					relret += 1
				else:
					ret += 1
			else:
				ret += 1
				#print("Maluuba found 'irrelevant' locations: "+str(maluLoc))
		except KeyError:
			if len(keyLoc) > 0:
				rel += 1
				#print('Maluuba found different locations: '+str(maluLoc))
			else:
				pass
				#print('Maluuba found no location entities in this article')
	#print('relret: '+str(relret))
	#print('rel: '+str(rel))
	#print('ret: '+str(ret))
	pr = relret/ret
	re = relret/rel
	print('Precision: '+str(pr))
	print('Recall: '+str(re))
	return (pr,re)
