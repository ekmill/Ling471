import pandas as pd
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


# Constants
ROUND = 4
GOOD_REVIEW = 1
BAD_REVIEW = 0
ALPHA = 1


def main(argv):
    test_true_pos = 0
    test_true_neg = 0
    test_false_pos = 0
    test_false_neg = 0
    train_true_pos = 0
    train_true_neg = 0
    train_false_pos = 0
    train_false_neg = 0

    data = pd.read_csv(argv[1])
    # print(data.head())
    train_data = data[:25000]
    test_data = data[25000:50000]

    # The next three lines are performing feature extraction and word counting.
    # They are choosing which words to count frequencies for, basically, to discard some of the noise.
    # TODO COMMENT: Add a general brief comment on why choosing which words to count may be important.
    tf_idf_vect = TfidfVectorizer(ngram_range=(1, 2))
    tf_idf_train = tf_idf_vect.fit_transform(X_train.values)
    tf_idf_test = tf_idf_vect.transform(X_test.values)

    # TODO COMMENT: The hyperparameter alpha is used for Laplace Smoothing.
    # Add a brief comment, trying to explain, in your own words, what smoothing is for.
    # You may want to read about Laplace smoothing here: https://towardsdatascience.com/laplace-smoothing-in-na%C3%AFve-bayes-algorithm-9c237a8bdece
    clf = MultinomialNB(alpha=ALPHA)
    # TODO COMMENT: Add a comment explaining in your own words what the "fit()" method is doing.
    clf.fit(tf_idf_train, y_train)

    # TODO COMMENT: Add a comment explaining in your own words what the "predict()" method is doing in the next two lines.
    y_pred_train = clf.predict(tf_idf_train)
    y_pred_test = clf.predict(tf_idf_test)

    X_train = train_data
    y_train =  pd.read_csv(X_train, usecols=['label', 'type'])
    X_test = test_data
    y_test = pd.read_csv(X_test, usecols=['label', 'type'])
    #compare to y_pred_train
    if y_train(type==0) and y_pred_train(type==0):
        train_true_neg +=1
    elif y_train(type==0) and y_pred_train(type==1):
        train_false_neg +=1
    elif y_train(type==1) and y_pred_train(type==1):
        train_true_pos +=1
    elif y_train(type==1) and y_pred_train(type==0):
        train_false_pos +=1
    if y_test(type==0) and y_pred_test(type==0):
        test_true_neg +=1
    elif y_test(type==0) and y_pred_test(type==1):
        test_false_neg +=1
    elif y_test(type==1) and y_pred_test(type==1):
        test_true_pos +=1
    elif y_test(type==1) and y_pred_test(type==0):
        test_false_pos +=1

    accuracy_test = (test_true_pos + test_true_neg) / (test_true_pos + test_true_neg + test_false_pos + test_false_neg)
    accuracy_train = (train_true_pos + train_true_neg) / (train_true_pos + train_true_neg + train_false_pos + train_false_neg)
    precision_pos_test, recall_pos_test = test_true_pos / (test_true_pos + test_false_neg), test_true_pos / (test_true_pos + test_false_pos)
    precision_neg_test, recall_neg_test = test_true_neg / (test_true_neg + test_false_pos), test_true_neg / (test_true_neg + test_false_neg)
    precision_pos_train, recall_pos_train = train_true_pos / (train_true_pos + train_false_neg), train_true_pos / (train_true_pos + train_false_pos)
    precision_neg_train, recall_neg_train = train_true_neg / (train_true_neg + train_false_pos), train_true_neg / (train_true_neg + train_false_neg)


    print("Train accuracy:           \t{}".format(round(accuracy_train, ROUND)))
    print("Train precision positive: \t{}".format(round(precision_pos_train, ROUND)))
    print("Train recall positive:    \t{}".format(round(recall_pos_train, ROUND)))
    print("Train precision negative: \t{}".format(round(precision_neg_train, ROUND)))
    print("Train recall negative:    \t{}".format(round(recall_neg_train, ROUND)))
    print("Test accuracy:            \t{}".format(round(accuracy_test, ROUND)))
    print("Test precision positive:  \t{}".format(round(precision_pos_test, ROUND)))
    print("Test recall positive:     \t{}".format(round(recall_pos_test, ROUND)))
    print("Test precision negative:  \t{}".format(round(precision_neg_test, ROUND)))
    print("Test recall negative:     \t{}".format(round(recall_neg_test, ROUND)))


if __name__ == "__main__":
    main(sys.argv)
