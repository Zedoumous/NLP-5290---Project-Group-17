import yake

from statistics import mean

def extractKeywordsYAKE(normalized_corpus):
    print('---YAKE Extraction---')
    print('------------------------\n')

    language = "en"
    max_ngram_size = 3
    deduplication_threshold = 0.9
    deduplication_algo = 'seqm'
    windowSize = 1
    numOfKeywords = 20

    kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
    keywords = kw_extractor.extract_keywords(normalized_corpus)

    zipped = list(map(list, zip(*keywords)))
    keywords = zipped[0]
    scores = zipped[1]

   
    for i, value in enumerate(keywords):
        print(value.ljust(40), scores[i])

    avg = mean(scores[:19])
    print("Score Average: " + str(avg))


    return keywords, scores, avg
