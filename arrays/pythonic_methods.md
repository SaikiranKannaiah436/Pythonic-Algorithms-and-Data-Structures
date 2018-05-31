# Important python methods to remember

* list.count() - Returns the number of occurances of value 

* collections.defaultdict() - Returns a dictionary object with first argument as the default value. Very useful to create complex data structures.

	```python
	corpus = "She saw Sharif's shoes on the sofa. But was she so sure those were Sharif's shoes she saw?"
	freq = defaultdict(int)
	for word in corpus.split():
		freq[word] += 1
	print(freq) # would print the frequency of each word in the corpus
	```
