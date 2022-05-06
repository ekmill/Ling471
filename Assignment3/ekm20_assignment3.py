
import re
import string
import sys
import pathlib as pl

'''
At the end of your program, output 5 numbers, one per line, rounded to 4 decimal points, in the exact following order:

Overall system accuracy
Precision wrt positive (training) reviews
Recall wrt positive (training) reviews
Precision wrt negative (training) reviews,
Recall wrt positive (training) reviews.
Do not output any text; we need just the numbers, for faster grading.
expected output:
0.2751
0.5558
0.3214
0.8072
0.2287
'''

#  these constants are return values for predict_simplistic and return end values.

POS_REVIEW = "POSITIVE"
NEG_REVIEW = "NEGATIVE"
NONE = "NONE"
POS = 'good'
NEG = 'bad'


# this method retrieves counts of good and bad, and returns what type of review it is.
def predict_simplistic(f):
    f() = argv[1]
    with open(f, 'r') as f:
        text = f.read()
    clean_text = text.translate(str.maketrans('', '', string.punctuation))
    clean_text = re.sub('\s+', ' ', clean_text)
    token_counts = {}
    tokens = clean_text.split()
    word_value = 0
    for word in tokens:
        if word not in token_counts:
            token_counts[word] = word_value
        elif word in token_counts:
            token_counts[word] += 1
    pos_count = token_counts.get(POS, 0)
    neg_count = token_counts.get(NEG, 0)
    if pos_count > neg_count:
        return POS_REVIEW
    elif neg_count > pos_count:
        return NEG_REVIEW
    else:
        return NONE


'''
TODO (1)
Refactor your assignment3.py program so that your main() function iterates over 
all files in both train/pos and train/neg directories, outputting a prediction for each file.
'''
def main(argv):

    # The file that you will read should be passed as the argument to the program.

    pos = pl.PosixPath('/Users/emma/Downloads/aclImdb/train/pos')
   # neg = pl.PosixPath('/Users/emma/Downloads/aclImdb/train/neg')
    for filename in pos():
        predict_simplistic(f)
   # for filename in neg():
    # Call the simplistic prediction function on the obtained counts.
    prediction = predict_simplistic()

    # Finally, let's print out what we predicted.
    print("The prediction for file {} is {}".format(filename, prediction))

if __name__ == "__main__":
    main(sys.argv)
