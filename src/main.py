# Imports
import pandas as pd     # load csv into DataFrame

###
### Hoping to get a better sense of the work flow and 
### and road map of the project by writing some helper functions. 
###

### Helper Functions

# Function to retrieve text data.
# (either 1 or more job postings or resumes)?
def getCorpus(filename):
    return pd.read_csv('../data/' + filename)

# Function to normalize text data. 
# (some skill extraction tools will normalize text for us; however, if not, this function is here)
# includes removing stopwords, punctuation, dates, links, etc...
def normalizeCorpus(corpus):
    pass

# Function to extract skill words from a given corpus.
# ideally, this function will output a set of skills extracted from the corpus
def extractSkills(corpus):
    pass

### Driver Code
if __name__ == '__main__':

    # display all 'Job_Desc' from all postings in 'Data_Job_TX.csv'
    print(getCorpus('Data_Job_TX.csv')['Job_Desc'])