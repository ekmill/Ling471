
import sys
import re
import string
from pathlib import Path

import pandas as pd
import csv

from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk import stem
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer


# Constants:
POS = 1
NEG = 0


def review_to_words(review, remove_stopwords=False, lemmatize=False):
    # Getting an off-the-shelf list of English "stopwords"
    stops = stopwords.words('english')
    # Initializing an instance of the NLTK stemmer/lemmatizer class
    sno = stem.SnowballStemmer('english')
    # Removing HTML using BeautifulSoup preprocessing package
    review_text = BeautifulSoup(review).get_text()
    # Remove non-letters using a regular expression
    review_text = re.sub("[^a-zA-Z]", " ", review_text)
    # Tokenizing by whitespace
    words = review_text.split()
    # Recall "list comprehension" from the lecture demo and try to understand what the below loops are doing:
    if remove_stopwords:
        words = [w for w in words if not w in stops]
    if lemmatize:
        lemmas = [sno.stem(w).encode('utf8') for w in words]
        # The join() function is a built-in method of strings.
        # The below says: iterate over the "lemmas" list and create
        # a new string where each item in "lemmas" is added to this new string,
        # and the items are separated by a space.
        # The b-thing is a quirk of the SnowballStemmer package.
        return b" ".join(lemmas)
    else:
        return ' '.join(words)


def cleanFileContents(f):
    with open(f, 'r', encoding='utf-8') as f:
        text = f.read()
    cleaned_text = review_to_words(text)
    lowercased = cleaned_text.lower()
    no_stop = review_to_words(lowercased, remove_stopwords=True)
    lemmatized = review_to_words(no_stop, lemmatize=True)
    return (text, cleaned_text, lowercased, no_stop, lemmatized)


def processFileForDF(f, table, label, t):
    text, cleaned_text, lowercased, no_stop, lemmatized = cleanFileContents(f)
    table.append([f.stem+'.txt', label, t, text,
                 cleaned_text, lowercased, no_stop, lemmatized])


def createDataFrames(argv):
    argv[1] = Path('../aclImdb/train/pos')
    argv[2] = Path('../aclImdb/train/neg')
    argv[3] = Path('../aclImdb/test/pos')
    argv[4] = Path('../aclImdb/test/neg')
    train_pos = list(Path(argv[1]).glob("*.txt"))
    train_neg = list(Path(argv[2]).glob("*.txt"))
    test_pos = list(Path(argv[3]).glob("*.txt"))
    test_neg = list(Path(argv[4]).glob("*.txt"))

    new_filename = "my_imdb_expanded.csv"
    column_names = ["file", "label", "type", "review"]
    df = pd.DataFrame(columns=column_names)
    for filename in train_pos:
        with open(filename, 'r') as f:
            file = filename
            review = cleanFileContents(filename)
            label = POS
            type = 'train'
            df.loc[len(df.index)] = [file, label, type, review]
    for filename in train_neg:
        with open(filename, 'r') as f:
            file = filename
            review = cleanFileContents(filename)
            label = NEG
            type = 'train'
            df.loc[len(df.index)] = [file, label, type, review]
    for filename in test_pos:
        with open(filename, 'r') as f:
            file = filename
            review = cleanFileContents(filename)
            label = POS
            type = 'test'
            df.loc[len(df.index)] = [file, label, type, review]
    for filename in test_neg:
        with open(filename, 'r') as f:
            file = filename
            review = cleanFileContents(filename)
            label = NEG
            type = 'test'
            df.loc[len(df.index)] = [file, label, type, review]

    data = []

    column_names = ["file", "label", "type", "review",
                    "cleaned_review", "lowercased", "no stopwords", "lemmatized"]
    df = pd.DataFrame(data=data, columns=column_names)
    df.sort_values(by=['type', 'file'])
    df.to_csv(new_filename)


def main(argv):
    createDataFrames(argv)


if __name__ == "__main__":
    main(sys.argv)
