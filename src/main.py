# Imports
import pandas as pd     # load csv into DataFrame

###
### Hoping to get a better sense of the work flow and 
### and road map of the project by writing some helper functions. 
###

### Helper Functions

# Function to retrieve text data.
# (either 1 or more job postings or resumes)?
def getCorpus(filename, dir):
    return pd.read_csv('../data/' + dir + '/' + filename)

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

    jpCorpus = getCorpus('Data_Job_TX.csv', 'job-postings')['Job_Desc']
    rCorpus  = getCorpus('kaggleResumes.csv', 'resumes')['Resume']

    # display all 'Job_Desc' from all postings in 'job-postings/Data_Job_TX.csv'
    print('DataFrame of Job Postings:')
    print(jpCorpus)

    print()

    # display all 'Resumes' from all resumes in 'resumes/kaggleResumes.csv'
    print('DataFrame of Resumes:')
    print(rCorpus)

    # extract skills here?
    normalizeCorpus(jpCorpus)
    extractSkills(jpCorpus)

    # keep going!
