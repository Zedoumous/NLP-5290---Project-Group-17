import jellyfish
from functools import reduce
import gensim
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
import re
import numpy as np

## Python Class to take the jp keywords and resume keywords and find the ones that are most similar
class SkillsMatching:
  def __init__(self, all_job_postings_keywords, all_resumes_keywords):
      self.all_job_postings_keywords = all_job_postings_keywords
      self.all_resumes_keywords = all_resumes_keywords

  # output JSON with matching job postings for each resume
  def skill_match(self):
      results = {"matching_job": []}
      for resume_json in self.all_resumes_keywords:
          # need to change this to match all text classifiers
          resume_keywords = resume_json["keywordsBERT"]
          scores = self.sim_score(self.all_job_postings_keywords, resume_keywords)
          # grab the index of the largest score in the arr
          max_idx = np.argmax(scores)
          results['matching_job'].append(self.all_job_postings_keywords[max_idx])

      return results

  def split_and_join_arr(self, arr):
    new_arr = []
    for w in arr:
      word_arr = re.split('\W+', w.lower())
      new_arr = new_arr + word_arr
    # print(new_arr)
    return new_arr
  
  def sim_score(self, docs, keywords):
    keywords = self.split_and_join_arr(keywords)
    gen_docs = [[w.lower() for w in word_tokenize(text)] 
            for text in docs]
    dictionary = gensim.corpora.Dictionary(gen_docs)
    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
    tf_idf = gensim.models.TfidfModel(corpus)
    sims = gensim.similarities.Similarity('/usr/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))

    query_doc_bow = dictionary.doc2bow(keywords)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    # print(sims[query_doc_tf_idf])
    return sims[query_doc_tf_idf]