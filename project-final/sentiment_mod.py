from nltk.tokenize import word_tokenize
from featureCollect import bag_of_words
import pickle
from nltk.corpus import wordnet

def sentiment(text):
    text = word_tokenize(text)
    text = [t for t in text if wordnet.synsets(t)]
    open_file = open("pickled_algos/mv_classifier", "rb")
    mv_classifier = pickle.load(open_file)
    open_file.close()
    feats = bag_of_words(text)
    return mv_classifier.classify(feats)

