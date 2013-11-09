
def main():
'''highest level: what are we doing?

	1. Create list of data input files
	2. Use each file to create a masterDictionary where keys are article id's and the values are lists of sentences in that article.
	3. Process the answer key files to create a similar dictionary as step 2, but the values contain the entities of the article
		(we will use a subset of the entities. Q: what data structure for the values of this dict?)
	4. For each article in masterDictionary:
		4a. send sentences to be interpreted by Maluuba API
		4b. synchronize format of response to compare to entities in answer key.
		4c. calculate precision/recall
		
'''