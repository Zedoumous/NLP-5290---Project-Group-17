# Imports
import pandas as pd     # pip install pandas. usage: loading data from csv files into dataframes

# From custom python file: keyBERTExtractor.py
from keyBERTExtractor import extractKeywordsBERT
# from CSOClassifierExtractor import extractKeywordsCSO
from YAKEextractor import YAKEextractor

### Helper Functions

# Function to retrieve text data.
# (either 1 or more job postings or resumes)?
def getFileData(filename, dir):
    return pd.read_csv('../data/' + dir + '/' + filename)

# Function to normalize text data. 
# (some skill extraction tools will normalize text for us; however, if not, this function is here)
# includes removing stopwords, punctuation, dates, links, etc...
def normalizeCorpus(corpus):
    pass

    # for now
    return corpus

# Function to extract skill words from a given corpus.
# ideally, this function will output a set of skills extracted from the corpus
def extractSkills(corpus):

    # run KeyBert Extraction
    keywordsBERT, scoresBERT = extractKeywordsBERT(corpus)

    # run CSO Classifier Extraction
    # keywordsCSO, scoresCSO   = extractKeywordsCSO(corpus)
    # extraction method 2
    keywords, scores = YAKEextractor(corpus)
    # extraction method n...
    # keep going!

### Driver Code
if __name__ == '__main__':

    # fetch the data
    job_posting_dataframe = getFileData('Data_Job_TX.csv'  , 'job-postings')
    resume_dataframe      = getFileData('kaggleResumes.csv', 'resumes'     )
    #---------------

    # print the dataframes
    print('DataFrame of Job Postings:')
    print(job_posting_dataframe)    
    print()

    print('DataFrame of Resumes:')
    print(resume_dataframe)
    print()
    #----------------------

    # fetch the job descriptions and resumes by themselves
    jpCorpus = list(job_posting_dataframe['Job_Desc'])
    rCorpus  = list(resume_dataframe['Resume'])
    #----------------------

    # Number of both job posting and resume samples to view
    NUM_SAMPLES = 5

    # for each JOB POSTING from the corpus
    i = 0
    for posting in jpCorpus:
        print('Job Posting #', i+1)
        print()

        text = normalizeCorpus(posting)
        extractSkills(text)

        # print lines, we are done with this posting
        print('------------------------\n')

        # break, after X postings
        i += 1
        if i > NUM_SAMPLES:
            break
    #---------------------- 

    # for each RESUME from the corpus
    i = 0
    for resume in rCorpus:
        print('Resume #', i+1)
        print()

        text = normalizeCorpus(resume)
        extractSkills(text)

        # print lines, we are done with this resume
        print('------------------------\n')

        # break, after X resumes
        i += 1
        if i > NUM_SAMPLES:
            break
    #---------------------- 

    
# keep going!

# end of driver code
#---------------

