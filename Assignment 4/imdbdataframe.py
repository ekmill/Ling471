
import pandas as pd
import sys
import string
import re
from pathlib import Path


train_pos = Path('/Users/emma/Downloads/aclImdb/train/pos')
train_neg = Path('/Users/emma/Downloads/aclImdb/train/neg')
test_pos = Path('/Users/emma/Downloads/aclImdb/test/pos')
test_neg = Path('/Users/emma/Downloads/aclImdb/test/neg')

def directory_list(argv):
    argv[1] = [f for f in train_pos.glob('*') if f.is_file]
    argv[2] = [f for f in train_neg.glob('*') if f.is_file]
    argv[3] = [f for f in test_pos.glob('*') if f.is_file]
    argv[4] = [f for f in test_neg.glob('*') if f.is_file]
    return argv[1, 2, 3, 4]

# Constants:
POS = 1
NEG = 0
n = 0

def createDataFrame(argv):
    new_filename = "my_imdb_dataframe.csv"
    column_names = ["file", "label", "type", "review"]
    df = pd.DataFrame(data=argv[1, 4], columns=column_names)
    for filename in directory_list(argv):
        with open(filename, 'r') as f:
            file = filename
            text = f.read()
            review = cleanFileContents(text)
            if 'pos' in Path:
                label = 'pos'
            else:
                label = 'neg'
            if 'train' in Path:
                type = 'train'
            else:
                type = 'test'
            df.loc[len(df.index)] = [file, label, type, review]

    # TODO: Create a single dataframe from the 4 IMBD directories (passed as argv[1]--argv[4]).
    # HINT: You when you are trying to get the pos/neg value and the test/train value,
    # you may want to use the `parts` attribute of a `Path` object


    df.to_csv(new_filename)


'''
The function below should be called on a file name.
It opens the file, reads its contents, and stores it in a variable.
Then, it removes punctuation marks, and returns the "cleaned" text.
'''


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
