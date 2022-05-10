
import re
import string
import sys
from pathlib import Path
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
def predict_simplistic(dir):
    true_pos = 0
    true_neg = 0
    false_pos = 0
    false_neg = 0
    pos = Path('/Users/emma/Downloads/aclImdb/train/pos')
    neg = Path('/Users/emma/Downloads/aclImdb/train/neg')
    pos_file = [f for f in pos.glob('*') if f.is_file]
    neg_file = [f for f in neg.glob('*') if f.is_file]
    for filename in pos_file:
        with open(filename, 'r') as f:
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
           # print("The prediction for file {} is POSITIVE".format(filename))
            true_pos += 1
        elif neg_count > pos_count:
           # print("The prediction for file {} is NEGATIVE".format(filename))
            false_neg += 1
       # else:
           # print("The prediction for file {} is NONE".format(filename))
         #   false_neg += 1
    for filename in neg_file:
        with open(filename, 'r', encoding='utf-8') as f:
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
           # print("The prediction for file {} is POSITIVE".format(filename))
            false_pos += 1
        elif neg_count > pos_count:
           # print("The prediction for file {} is NEGATIVE".format(filename))
            true_neg += 1
       # else:
           # print("The prediction for file {} is NONE".format(filename))
          #  false_pos += 1
    print(true_pos, true_neg, false_pos, false_neg)

def main(argv):
    filename = argv[1]
    # The file that you will read should be passed as the argument to the program.
    prediction = predict_simplistic(dir)


if __name__ == "__main__":
    main(sys.argv)
