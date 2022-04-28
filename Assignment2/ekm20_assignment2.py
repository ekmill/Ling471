
# Import the system module
import sys

# Import regular expressions module
import re

# Import the string module to access its punctuation set
import string

#  these constants are return values for predictSimplistic and return end values.

POS_REVIEW = "POSITIVE"
NEG_REVIEW = "NEGATIVE"
NONE = "NONE"
POS = 'good'
NEG = 'bad'


'''
 The below function should be called on a file name.
 It should open the file, read its contents, and store it in a variable.
 Then it should remove punctuation marks and return the "cleaned" text.
'''


def cleanfilecontents(f):
    # The below two lines open the file and read all the text
    # You do not need to modify the below two lines; they are already working as needed.
    with open(f, 'r') as f:
        text = f.read()

    # The below line will clean the text of punctuation marks.
    clean_text = text.translate(str.maketrans('', '', string.punctuation))

    # replaces all tabs with spaces, and also all occurrences of more than one space in a row with a single space.
    clean_text = re.sub('\s+', ' ', text)
    return clean_text


'''
The below function takes a string as input, breaks it down into word tokens by space, and stores, in a dictionary table,
how many times each word occurred in the text. It returns the token_counts dictionary table.
'''


def count_tokens(clean_text):
    token_counts = {}
    tokens = clean_text.split()
    word_value = 1
    for word in tokens:
        if word not in token_counts:
            token_counts[word] = word_value
        else:
            token_counts.update(word=word_value + 1)
    print (token_counts)
    return token_counts


'''
This prediction function will do the following rudimentary data science:
If a review contains more of the word "good" than of the word "bad", 
the function predicts "positive" (by returning the string "POSITIVE").
If the count is equal (note that this includes zero count),
the function cannot make a prediction and returns a string "NONE".
'''


# this method retrieves counts of good and bad, and returns what type of review it is.
def predict_simplistic(token_counts):
    pos_count = token_counts.get(POS, 0)
    neg_count = token_counts.get(NEG, 0)
    if pos_count > neg_count:
        return POS_REVIEW
    elif neg_count > pos_count:
        return NEG_REVIEW
    else:
        return NONE


'''
The main function is the entry point of the program.
When debugging, if you want to start from the very beginning,
start here.
'''


def main(argv):
    # The file that you will read should be passed as the argument to the program.
    filename = argv[1]

    # Now, we will call cleanFileContents on the filename we were passed.
    clean_text = cleanfilecontents(filename)

    # Now, we will count how many times each word occurs in the review.
    # We assign the output of the function to a new variable we call tokens_with_counts.
    tokens_with_counts = count_tokens(clean_text)

    # Call the simplistic prediction function on the obtained counts.
    # Store the output of the function in a new variable called "prediction".
    prediction = predict_simplistic(tokens_with_counts)

    # Finally, let's print out what we predicted.
    print("The prediction for file {} is {}".format(filename, prediction))

if __name__ == "__main__":
    main(sys.argv)