# Modified Blog Authorship Dataset

This data is sourced from the "Blog Authorship Corpus", available [here](http://u.cs.biu.ac.il/~koppel/BlogCorpus.htm). The original dataset was tokenized and split into sentences using [spacy](https://spacy.io/). Number-like tokens were replaced by "<#>". Tokens other than the 9999 most common tokens were replaced by "<UNK>", for a vocabulary of 10000 words. Sentences were tagged with the gender (0 for male, 1 for female) and age bracket (0 for teens, 1 for 20s, 2 for 30s) and placed into a pandas dataframe. 
