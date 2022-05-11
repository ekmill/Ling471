
import re
import string
import sys
from pathlib import Path

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
    nonepos = 0
    noneneg = 0
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
        word_value = 1
        for word in tokens:
            if word not in token_counts:
                token_counts[word] = word_value
            elif word in token_counts:
                token_counts[word] += 1
        pos_count = token_counts.get(POS, 0)
        neg_count = token_counts.get(NEG, 0)
        if pos_count > neg_count:
            true_pos += 1
        elif neg_count > pos_count:
            false_pos += 1
        else:
           nonepos += 1
    for filename in neg_file:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
        clean_text = text.translate(str.maketrans('', '', string.punctuation))
        clean_text = re.sub('\s+', ' ', clean_text)
        token_counts = {}
        tokens = clean_text.split()
        word_value = 1
        for word in tokens:
            if word not in token_counts:
                token_counts[word] = word_value
            elif word in token_counts:
                token_counts[word] += 1
        pos_count = token_counts.get(POS, 0)
        neg_count = token_counts.get(NEG, 0)
        if pos_count > neg_count:
            false_neg += 1
        elif neg_count > pos_count:
            true_neg += 1
        else:
           noneneg += 1
    accuracy = (true_pos + true_neg)/(true_pos + true_neg + false_pos + false_neg + noneneg + nonepos)
    round(accuracy, 4)
    pos_precision = true_pos/(true_pos + false_neg)
    round(pos_precision, 4)
    pos_recall = true_pos/(true_pos + false_pos + nonepos)
    round(pos_recall, 4)
    neg_precision = true_neg/(true_neg + false_pos)
    round(neg_precision, 4)
    neg_recall = true_neg/(true_neg + false_neg + noneneg)
    round(neg_recall, 4)


def main(argv):
    filename = argv[1]
    # The file that you will read should be passed as the argument to the program.
    prediction = predict_simplistic(dir)
    return prediction


if __name__ == "__main__":
    main(sys.argv)
