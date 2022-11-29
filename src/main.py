# Imports
import pandas as pd     # pip install pandas. usage: loading data from csv files into dataframes
import nltk
from nltk.tokenize import word_tokenize  
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download("all")

# From custom python file: keyBERTExtractor.py
from keyBERTExtractor import extractKeywordsBERT
from CSOClassifierExtractor import extractKeywordsCSO
from YAKEextractor import extractKeywordsYAKE
from SkillMatching import SkillsMatching

### Helper Functions

# Function to retrieve text data.
# (either 1 or more job postings or resumes)?
def getFileData(filename, dir):
    return pd.read_csv('data/' + dir + '/' + filename)

# Function to normalize text data. 
# (some skill extraction tools will normalize text for us; however, if not, this function is here)
# includes removing stopwords, punctuation, dates, links, etc...
def normalizeCorpus(corpus):
    return corpus
    # need to fix this 
    # nltk_tokenList = word_tokenize(corpus)
    # lemmatizer = WordNetLemmatizer()
    # nltk_lemmaList = []
    # for word in nltk_tokenList:
    #     nltk_lemmaList.append(lemmatizer.lemmatize(word))

    # normalized_corpus = []  
    # nltk_stop_words = set(stopwords.words("english"))
    # for w in nltk_lemmaList:  
    #     if w not in nltk_stop_words:  
    #         normalized_corpus.append(w)

    # punctuation = ";:.,?!"
    # for word in normalized_corpus:
    #     if word in punctuation:
    #         normalized_corpus.remove(word)

    #still need to add dates and links
    # return normalized_corpus

# Function to extract skill words from a given corpus.
# ideally, this function will output a set of skills extracted from the corpus
def extractSkills(corpus):

    # run KeyBert Extraction
    keywordsBERT, scoresBERT = extractKeywordsBERT(corpus)

    # run CSO Classifier Extraction
    keywordsCSO              = extractKeywordsCSO(corpus)
    
    # extraction method 2
    keywordsYAKE, scoresYAKE = extractKeywordsYAKE(corpus)
    # extraction method n...
    # keep going!
    return {"keywordsBERT": keywordsBERT,
            "keywordsCSO": keywordsCSO,
            "keywordsYAKE": keywordsYAKE}

### Driver Code
if __name__ == '__main__':

    # fetch the data
    job_posting_dataframe = getFileData('Data_Job_TX.csv'  , 'job-postings')
    resume_dataframe      = getFileData('kaggleResumes.csv', 'resumes'     )
    #---------------

    '''
    # print the dataframes
    print('DataFrame of Job Postings:')
    print(job_posting_dataframe)    
    print()

    print('DataFrame of Resumes:')
    print(resume_dataframe)
    print()
    #----------------------
    '''

    # fetch the job descriptions and resumes by themselves
    jpCorpus = list(job_posting_dataframe['Job_Desc'])
    rCorpus  = list(resume_dataframe['Resume'])
    #----------------------

    # Number of both job posting and resume samples to view
    NUM_SAMPLES = 10

    # for each JOB POSTING from the corpus
    i = 0
    all_job_postings = []
    for posting in jpCorpus:
        print('Job Posting #', i+1)
        print()

        text = normalizeCorpus(posting)
        job_posting_json = extractSkills(text)
        all_job_postings.append(text)
        # print lines, we are done with this posting
        print('------------------------\n')

        # break, after X postings
        i += 1
        if i > NUM_SAMPLES:
            break
    #---------------------- 

    # for each RESUME from the corpus
    i = 0
    all_resumes_keywords = []
    for resume in rCorpus:
        print('Resume #', i+1)
        print()

        text = normalizeCorpus(resume)
        resume_json = extractSkills(text)
        all_resumes_keywords.append(resume_json)
        # print lines, we are done with this resume
        print('------------------------\n')

        # break, after X resumes
        i += 1
        if i > NUM_SAMPLES:
            break
    #---------------------- 
    # Resume and Job Posting Matching
    matching = SkillsMatching(all_job_postings, all_resumes_keywords)
    match_job_postings = matching.skill_match()
    # print(match_job_postings)
    for i, jp in enumerate(match_job_postings['matching_job']):
        i += 1
        print('------------------------\n')
        print("Matching Job Posting for Resume %s" % i)
        print(jp)

    
# keep going!

# end of driver code
#---------------