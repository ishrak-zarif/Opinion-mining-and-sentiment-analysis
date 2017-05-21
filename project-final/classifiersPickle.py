from project.featureCollect import high_information_words, bag_of_words_in_set, label_feats_from_corpus, split_label_feats, bag_of_words

from nltk.corpus import movie_reviews

from nltk.classify import NaiveBayesClassifier

from nltk.classify import DecisionTreeClassifier

from nltk.classify.scikitlearn import  SklearnClassifier

from sklearn.svm import LinearSVC

from nltk.classify.util import accuracy

from project.classification import MaxVoteClassifier

import pickle

labels = movie_reviews.categories()

labeled_words = [(l,movie_reviews.words(categories=[l])) for l in labels]

high_info_words = set(high_information_words(labeled_words))

save_high_info_words = open("pickled_algos/high_info_words","wb")
pickle.dump(high_info_words, save_high_info_words)
save_high_info_words.close()


feat_det = lambda words: bag_of_words_in_set(words, high_info_words)

lfeats = label_feats_from_corpus(movie_reviews, feature_detector=feat_det)

save_lfeats = open("pickled_algos/lfeats","wb")
pickle.dump(lfeats, save_lfeats)
save_lfeats.close()


train_feats, test_feats = split_label_feats(lfeats)

save_train_feats = open("pickled_algos/train_feats","wb")
pickle.dump(train_feats, save_train_feats)
save_train_feats.close()


save_test_feats = open("pickled_algos/test_feats","wb")
pickle.dump(test_feats, save_test_feats)
save_test_feats.close()


nb_classifier = NaiveBayesClassifier.train(train_feats)

print(accuracy(nb_classifier, test_feats))

save_nb_classifier = open("pickled_algos/nb_classifier","wb")
pickle.dump(nb_classifier, save_nb_classifier)
save_nb_classifier.close()

dt_classifier = DecisionTreeClassifier.train(train_feats)

print(accuracy(dt_classifier, test_feats))

save_dt_classifier = open("pickled_algos/dt_classifier","wb")
pickle.dump(dt_classifier, save_dt_classifier)
save_dt_classifier.close()

sk_classifier = SklearnClassifier(LinearSVC()).train(train_feats)

print(accuracy(sk_classifier, test_feats))

save_sk_classifier = open("pickled_algos/sk_classifier","wb")
pickle.dump(sk_classifier, save_sk_classifier)
save_sk_classifier.close()

mv_classifier = MaxVoteClassifier(nb_classifier, dt_classifier, sk_classifier)

print(accuracy(mv_classifier, test_feats))

save_mv_classifier = open("pickled_algos/mv_classifier","wb")
pickle.dump(mv_classifier, save_mv_classifier)
save_mv_classifier.close()


def sentiment(text):
    feats = bag_of_words(text)
    return mv_classifier.classify(feats)

