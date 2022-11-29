from summa import keywords
from statistics import mean

def extractKeywordsTextRank(normalized_corpus):
  print('\n')
  print('---TextRank Extraction---')
  print('------------------------\n')

  #extract
  TR_keywords = keywords.keywords(normalized_corpus, scores=True)

  #zip into list
  zipped = list(map(list, zip(*TR_keywords)))
  TR_keywords = zipped[0]
  scores = zipped[1]
  

  #print(TR_keywords[0:20])
  print('-Skill-'.ljust(40), '-Score-')
  for i, value in enumerate(TR_keywords[0:19]):
    print(value.ljust(40), scores[i])
    
  avg = mean(scores[:19])
  print("Score Average: " + str(avg))
  
  

  return TR_keywords, scores, avg
  
  
