
import pandas as pd
import sys
import string
import re
from pathlib import Path


pos_train = Path('/Users/emma/Downloads/aclImdb/train/pos')
neg_train = Path('/Users/emma/Downloads/aclImdb/train/neg')
pos_test = Path('/Users/emma/Downloads/aclImdb/test/pos')
neg_test = Path('/Users/emma/Downloads/aclImdb/test/neg')

# Constants:
POS = 1
NEG = 0


def createDataFrame(argv):
    pos_train_files = [f for f in pos_train.glob('*') if f.is_file]
    neg_train_files = [f for f in neg_train.glob('*') if f.is_file]
    pos_test_files = [f for f in pos_test.glob('*') if f.is_file]
    neg_test_files = [f for f in neg_test.glob('*') if f.is_file]
    new_filename = "my_imdb_dataframe.csv"
    column_names = ["file", "label", "type", "review"]
    df = pd.DataFrame(columns=column_names)
    for filename in pos_train_files:
        with open(filename, 'r', encoding='utf-8') as f:
            file = filename
            review = cleanFileContents(f)
            label = 'pos'
            type = 'train'
            df.loc[len(df.index)] = [file, label, type, review]
    for filename in neg_train_files:
        with open(filename, 'r', encoding='utf-8') as f:
            file = filename
            text = f.read()
            review = cleanFileContents(text)
            label = 'neg'
            type = 'train'
            df.loc[len(df.index)] = [file, label, type, review]
    for filename in pos_test_files:
        with open(filename, 'r', encoding='utf-8') as f:
            file = filename
            text = f.read()
            review = cleanFileContents(text)
            label = 'pos'
            type = 'test'
            df.loc[len(df.index)] = [file, label, type, review]
    for filename in neg_test_files:
        with open(filename, 'r', encoding='utf-8') as f:
            file = filename
            review = cleanFileContents(f)
            label = 'neg'
            type = 'test'
            df.loc[len(df.index)] = [file, label, type, review]
    df.to_csv(new_filename)


def cleanFileContents(f):
    with open(f, 'r', encoding='utf-8') as f:
        text = f.read()
    clean_text = text.translate(str.maketrans('', '', string.punctuation))
    clean_text = re.sub(r'\s+', ' ', clean_text)
    return clean_text


def main(argv):
    createDataFrame(argv)


if __name__ == "__main__":
    main(sys.argv)
