import nltk
nltk.download('stopwords')
from cso_classifier import CSOClassifier      # import classifier tool

# update the most recent model
CSOClassifier.update() 

# define the model object
CSO_Extractor = CSOClassifier(modules = "both", enhancement = "first", explanation = False)

def extractKeywordsCSO(normalized_corpus):

  # run the extraction
  result = CSO_Extractor.run(normalized_corpus)

  print('-----CSO Extraction-----')
  print('------------------------\n')
  
  for keyword in result['union']:
    print(keyword)

  return result['union']
  

