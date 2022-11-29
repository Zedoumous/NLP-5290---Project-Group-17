# Imports
from keybert import KeyBERT # pip install keybert (give it a minute...)

'''
/*---------------------------------------------------------------------
 |  Method: extractKeywordsBERT
 |
 |  Purpose: Uses the KeyBert Keyword Extraction Tool to extract
 |           and return keywords from a given corpus. 
 |      
 |  Author: Tyler Parks
 |  Created On: 10/30/22
 |
 |  Parameters:
 |      normalized_corpus -- A single string containing all text of the
 |                           normalized corpus.
 |
 |  Returns: 
 |      keywords -- List of collected keywords
 |      scores -- List of those keyword's scores
 |
 |  References: https://maartengr.github.io/KeyBERT/#usage
 |
 *-------------------------------------------------------------------*/
''' 
def extractKeywordsBERT(normalized_corpus):   
    print('---KeyBert Extraction---')
    print('------------------------\n')

    # init. language model 
    language_model = KeyBERT(model = 'all-mpnet-base-v2')

    # extract those keywords!
    data = language_model.extract_keywords( normalized_corpus, 
                                            keyphrase_ngram_range=(1, 3), 
                                            stop_words='english',
                                            use_maxsum=False, 
                                            use_mmr=True,
                                            diversity=0.7,
                                            nr_candidates=20, 
                                            top_n=15
                                        )

    # zip the lists
    zipped = list(map(list, zip(*data)))
    keywords = zipped[0]
    scores = zipped[1]

    print('-Skill-'.ljust(40), '-Score-')
    for i, value in enumerate(keywords):
        print(value.ljust(40), scores[i])
    print()

    return keywords, scores