# Skeleton for Assignment_4.
# Ling471 Spring 2021.
from operator import itemgetter
import pandas as pd
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import keras_preprocessing

# Constants
ROUND = 4
GOOD_REVIEW = 1
BAD_REVIEW = 0
ALPHA = 1

def calculations(data):
    test_true_pos = 0
    test_true_neg = 0
    test_false_pos = 0
    test_false_neg = 0
    train_true_pos = 0
    train_true_neg = 0
    train_false_pos = 0
    train_false_neg = 0

    train_data = data[:25000]
    test_data = data[25000:50000]

    y_train = itemgetter(1)
    y_test = itemgetter(2)
    X_train = dict(train_data.items(), key=y_train)
    X_test = dict(test_data.items(), key=itemgetter(2))

def decode_review(X_train, X_test):
    index = dict([(value, key) for (key, value) in X_train.items()])
    tf_idf_vect = TfidfVectorizer(ngram_range=(1, 2))
    tf_idf_train = tf_idf_vect.fit_transform(X_train.values)
    tf_idf_test = tf_idf_vect.transform(X_test.values)
    clf = MultinomialNB(alpha=ALPHA)
    clf.partial_fit(tf_idf_train[:12500], y_train[:12500], classes=[0, 1])
    clf.partial_fit(tf_idf_train[12500:25000], y_train[12500:25000])

    y_pred_train = clf.predict(tf_idf_train)
    y_pred_test = clf.predict(tf_idf_test)


    for value in y_train:
        for yvalue in y_pred_train:
            if value ==0 and yvalue == 0:
                train_true_neg +=1
                print('train_true_neg is: {}'.format(train_true_neg))
            elif value == 0 and yvalue == 1:
                train_false_neg +=1
                print('train_false_neg is: {}'.format(train_false_neg))
            elif value == 1 and yvalue == 1:
                train_true_pos +=1
                print('train_true_pos is: {}'.format(train_true_pos))
            elif value == 1 and yvalue == 0:
                train_false_pos +=1
                print('train_false_pos is: {}'.format(train_false_pos))
    for value in y_test:
        if X_test(value==0) and y_pred_test(value==0):
            test_true_neg +=1
        elif X_test(value==0) and y_pred_test(value==1):
            test_false_neg +=1
        elif X_test(value==1) and y_pred_test(value==1):
            test_true_pos +=1
        elif X_test(value==1) and y_pred_test(value==0):
            test_false_pos +=1
    # if it works up to here, consider making a separate function for the below equations and using that in A5
    accuracy_test = (test_true_pos + test_true_neg) / (test_true_pos + test_true_neg + test_false_pos + test_false_neg)
    accuracy_train = (train_true_pos + train_true_neg) / (
    train_true_pos + train_true_neg + train_false_pos + train_false_neg)
    precision_pos_test, recall_pos_test = test_true_pos / (test_true_pos + test_false_neg), test_true_pos / (
    test_true_pos + test_false_pos)
    precision_neg_test, recall_neg_test = test_true_neg / (test_true_neg + test_false_pos), test_true_neg / (
    test_true_neg + test_false_neg)
    precision_pos_train, recall_pos_train = train_true_pos / (train_true_pos + train_false_neg), train_true_pos / (
    train_true_pos + train_false_pos)
    precision_neg_train, recall_neg_train = train_true_neg / (train_true_neg + train_false_pos), train_true_neg / (
    train_true_neg + train_false_neg)

    # Report the metrics via standard output.
    # Please DO NOT modify the format (for grading purposes).
    # You may change the variable names of course, if you used different ones above.

    print("Train accuracy:           \t{}".format(round(accuracy_train, ROUND)))
    print("Train precision positive: \t{}".format(
        round(precision_pos_train, ROUND)))
    print("Train recall positive:    \t{}".format(
        round(recall_pos_train, ROUND)))
    print("Train precision negative: \t{}".format(
        round(precision_neg_train, ROUND)))
    print("Train recall negative:    \t{}".format(
        round(recall_neg_train, ROUND)))
    print("Test accuracy:            \t{}".format(round(accuracy_test, ROUND)))
    print("Test precision positive:  \t{}".format(
        round(precision_pos_test, ROUND)))
    print("Test recall positive:     \t{}".format(
        round(recall_pos_test, ROUND)))
    print("Test precision negative:  \t{}".format(
        round(precision_neg_test, ROUND)))
    print("Test recall negative:     \t{}".format(
        round(recall_neg_test, ROUND)))


def main(data):
    data = pd.read_csv(data, usecols=['column'])
    calculations(data)
    decode_review(X_train, X_test)


if __name__ == "__main__":
    main(sys.argv)
