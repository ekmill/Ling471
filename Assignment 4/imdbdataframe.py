
import pandas as pd
import sys
import string
import re
from pathlib import Path


train_pos = Path('/Users/emma/Downloads/aclImdb/train/pos')
train_neg = Path('/Users/emma/Downloads/aclImdb/train/neg')
test_pos = Path('/Users/emma/Downloads/aclImdb/test/pos')
test_neg = Path('/Users/emma/Downloads/aclImdb/test/neg')

def directory_list(train_pos, train_neg, test_pos, test_neg):
    train_pos_file = [f for f in train_pos.glob('*') if f.is_file]
    train_neg_file = [f for f in train_neg.glob('*') if f.is_file]
    test_pos_file = [f for f in test_pos.glob('*') if f.is_file]
    test_neg_file = [f for f in test_neg.glob('*') if f.is_file]
    argv = [train_pos_file, train_neg_file, test_pos_file, test_neg_file]
    return argv

# Constants:
POS = 1
NEG = 0


def createDataFrame(argv):
    new_filename = "my_imdb_dataframe.csv"
    # TODO: Create a single dataframe from the 4 IMBD directories (passed as argv[1]--argv[4]).
    df = pd.DataFrame(argv, columns=['File', 'Label', 'Type', 'Review'])
    # For example, "data" can be a LIST OF LISTS.
    # In this case, each list is a set of column values, e.g. ["0_2.txt", "neg", "test", "Once again Mr Costner..."].
    # That is, each list represents a single row in your data frame.
    # You may use a different way of creating a dataframe so long as the result is accurate.
    # TODO: Call the cleanFileContents() function on each file, as you are iterating over them.
    data = []
    # Your code here...
    # Try to create a list of lists, for example, as illustrated above.
    # Consider writing a separate function which takes a filename and returns a list representing the reivew vector.
    # This will make your code here cleaner.
    # HINT: You when you are trying to get the pos/neg value and the test/train value,
    # you may want to use the `parts` attribute of a `Path` object

    # Once you are done, the code below will only require modifications if your data variable is not a list of lists.
    # Sample column names; you can use different ones if you prefer,
    # but then make sure to make appropriate changes in assignment4_skeleton.py.
    column_names = ["file", "label", "type", "review"]
    # Sample way of creating a dataframe. This assumes that "data" is a LIST OF LISTS.
    df = pd.DataFrame(data=data, columns=column_names)
    # Saving to a file:
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
