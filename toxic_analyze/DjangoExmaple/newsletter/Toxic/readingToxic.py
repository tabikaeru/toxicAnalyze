import pandas as pd, numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import matplotlib as plt
import re, string
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.grid_search import GridSearchCV
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score
import os
def checkingToxic(checkText):
  print(os.getcwd())
  train = pd.read_csv(os.getcwd() + '/newsletter/Toxic/input/train.csv')


  lens = train.comment_text.str.len()
  lens.mean(), lens.std(), lens.max()
  lens.hist()



  label_cols = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
  train['none'] = 1-train[label_cols].max(axis=1)
  train.describe()


  COMMENT = 'comment_text'
  train[COMMENT].fillna("unknown", inplace=True)



  pattern = r"ca"
  text = "caabsacasca"
  repatter = re.compile(pattern)
  matchOB = repatter.match(text)
  hoge = "“”¨«»®´·º½¾¿¡§£₤‘’"
  re_tok = re.compile(hoge)
  exWord = '!"#$%&\'()\*\+,-./:;<=>@\]^_`{|}~“”¨«»®´·º½¾¿¡§£₤‘’\[\?'
  re_tok = re.compile(exWord)

  def tokenize(s): return re_tok.sub(r' \1 ', s).split()

  vec = TfidfVectorizer(ngram_range=(1,2), tokenizer=tokenize,
                 min_df=3, max_df=0.9, strip_accents='unicode', use_idf=1,
                 smooth_idf=1, sublinear_tf=1 )
  trn_term_doc = vec.fit_transform(train[COMMENT])
  trn_term_doc = test_term_doc = train = 0




  #convert a text for tdf
  texts = []
  texts.append(checkText)
  textsdf =  pd.Series(texts)
  textTransform = vec.transform(texts)

  toxicLabel = ["identity_hate", "obscene", "threat", "insult", "severe_toxic", "toxic"]
  results = []
  results.append(toxicLabel)
  results.append([])
  for itr in range(len(toxicLabel)):
    # readning classifier

    classifier = joblib.load(os.getcwd() + '/newsletter/Toxic/learningMachine/logsitic_' + str(toxicLabel[itr]) +'.pkl.cmp')

    #estimating 
    
    #hogeTest = vec.transform(test[COMMENT])
    pr_labels = classifier.predict(textTransform)
    results[1].append(pr_labels[0])
  return results[1]



if __name__ == '__main__':
  checkingToxic(checkText = "test_term_doc")
