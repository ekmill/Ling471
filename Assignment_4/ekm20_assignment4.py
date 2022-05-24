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
    # Read in the data.
    data = pd.read_csv(argv[1])
    # print(data.head())

    train_data = data[:25000]

    test_data = data[25000:50000]

    X_train = train_data
    y_train =  pd.read_csv(X_train, usecols=['label'])
    X_test = test_data
    y_test = pd.read_csv(X_test, usecols=['label'])

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

    # TODO: Compute accuracy, precision, and recall, for both train and test data.
    # Import and call your methods from evaluation.py (or wherever) which you wrote for HW3.
    # Note: If you methods there accept lists, you will probably need to cast your pandas label objects to simple python lists:
    # e.g. list(y_train) -- when passing them to your accuracy and precision and recall functions.

    accuracy_test = (true_pos + true_neg) / (true_pos + true_neg + false_pos + false_neg + noneneg + nonepos)
    accuracy_train = (true_pos + true_neg) / (true_pos + true_neg + false_pos + false_neg + noneneg + nonepos)
    precision_pos_test, recall_pos_test = true_pos / (true_pos + false_neg), true_pos / (true_pos + false_pos + nonepos)
    precision_neg_test, recall_neg_test = true_neg / (true_neg + false_pos), true_neg / (true_neg + false_neg + noneneg)
    precision_pos_train, recall_pos_train = true_pos / (true_pos + false_neg) true_pos / (true_pos + false_pos + nonepos)
    precision_neg_train, recall_neg_train = true_neg / (true_neg + false_pos), true_neg / (true_neg + false_neg + noneneg)


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
