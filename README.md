Information Extraction using the Maluuba API
====================

Members: David Greis, Khoa Tran

Option 2: Explore the Maluuba API and determine how it works on a collection

Corpus: *describe what and where did we find the corpus*

### Motivation behind the code

### Challenges

### Responsibility of each member

* David worked on making a master dictionary from the test data, where 
a key of the dict is the article ID, and the corresponding value is a 
list of sentences to be interpreted by the Malluba API one by one.

He also worked on determining the precision and recall [fill in the rest 
here]

* Khoa worked on making the test dictionary given the entities and their 
values. Each key in the dictionary is the article ID as in the master 
dictionary, while each value is another dictionary of entities, which 
follows the format: {entity_name: entity_value}, e.g. {'city': Berkeley}. 

He also worked on sending request to the Maluuba API and extracting the 
response based on the sentences curated by David. The result is then 
compared and contrasted with the test dictionary to determine the 
accuracy of the API and how well it works on the input data of 400 articles. 
