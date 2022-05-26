import pandas as pd
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


# Constants
ROUND = 4
GOOD_REVIEW = 1
BAD_REVIEW = 0
ALPHA = 1


def recall_precision_accuracy(data):
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
    X_train = train_data
    y_train = train_data.type
    X_test = test_data
    y_test = test_data.type

    '''choosing which words to count is important to the basis of predictions and to eliminate noise while finding
    relevant tokens. Some more frequent function words may be less useful to the analysis, while words that occur only 
    once may be completely irrelevant to the positive/negative analysis. This was seen in the error analysis part of 
    assignment 3.'''
    tf_idf_vect = TfidfVectorizer(ngram_range=(1, 2))
    tf_idf_train = tf_idf_vect.fit_transform(X_train.values)#stops working at this row. error is 'numpy.ndarray' object has no attribute 'lower'.
                                                            #tried for hours to fix this and can't.
    tf_idf_test = tf_idf_vect.transform(X_test.values)

    '''Laplace Smoothing is important for naive Bayes analysis. It essentially provides an extra value to the NB formula
    so as to avoid zero-values of words coming up in the test data. This would lead to negative infinities, which 
    effectively break our analysis.'''
    clf = MultinomialNB(alpha=ALPHA)
    clf.fit(tf_idf_train, y_train)

    '''the predict() method is taking the fits from the lines above and creating predict values for both the test and 
    train data. this will then be compared with the actual y_train and y_test types during the analysis of accuracy,
    precision and recall.'''
    y_pred_train = clf.predict(tf_idf_train)
    y_pred_test = clf.predict(tf_idf_test)

    for row in X_train:
        if y_train(type==0) and y_pred_train(type==0):
            train_true_neg +=1
        elif y_train(type==0) and y_pred_train(type==1):
            train_false_neg +=1
        elif y_train(type==1) and y_pred_train(type==1):
            train_true_pos +=1
        elif y_train(type==1) and y_pred_train(type==0):
            train_false_pos +=1
    for row in X_test:
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


def main(argv):
    data = pd.read_csv(argv[1])
    recall_precision_accuracy(data)


if __name__ == "__main__":
    main(sys.argv)
