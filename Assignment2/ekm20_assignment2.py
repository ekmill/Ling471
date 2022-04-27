

# Import the system module
import sys

# Import regular expressions module
import re

# Import the string module to access its punctuation set
import string

# The below function should be called on a file name.
# It should open the file, read its contents, and store it in a variable.
# Then it should remove punctuation marks and return the "cleaned" text.

def cleanFileContents(f):
    # The below two lines open the file and read all the text from it
    # storing it into a variable called "text".
    # You do not need to modify the below two lines; they are already working as needed.
    with open(f, 'r') as f:
        text = f.read()

    # The below line will clean the text of punctuation marks.
    # Ask if you are curious about how it works! But you can just use it as is.
    # Observe the effect of the function by inspecting the debugger pane while stepping over.
    clean_text = text.translate(str.maketrans('', '', string.punctuation))

    # replaces all tabs with spaces, and also all occurrences of more than one
    # space in a row with a single space.

    # TODO: replace all tabs with spaces. check 1
    clean_text = str.replace('\s+', ' ' , text)
    return clean_text


'''
The below function takes a string as input, breaks it down into word tokens by space, and stores, in a dictionary table,
how many times each word occurred in the text. It returns the dictionary table.
'''


def countTokens(text):
    token_counts = {}

    #takes text and splits into tokens

    tokens = text.split()

# Inside the loop, so, for each word, we will perform some conditional logic:
# If the word is not yet stored in the dictionary that
# we called "token_counts" as a key, we will store it there now,
# and we will initialize the key's value to 0.
# Outside that if statement: now that we are sure
# the word is stored as a key, we will increment the count by 1.

    value = 0

    for tokens in text:
        if tokens not in token_counts:
            token_counts[tokens] = value
        else:
            token_counts[tokens] = value + 1
    return token_counts


'''
This silly "prediction function" will do the following "rudimentary data science":
If a review contains more of the word "good" than of the word "bad", 
the function predicts "positive" (by returning a string "POSITIVE").
If it contains more of the word "bad" than of the word "good",
the function predicts "negative". 
If the count is equal (note that this includes zero count),
the function cannot make a prediction and returns a string "NONE".
'''

# Constants. Constants are important to avoid typo-related bugs, among other reasons.
# Use these constants as return values for the below function.

POS_REVIEW = "POSITIVE"
NEG_REVIEW = "NEGATIVE"
NONE = "NONE"
POS = 'good'
NEG = 'bad'

#this method retrieves counts of good and bad, and returns what type of review it is.
def predictSimplistic(counts):
    pos_count = counts.get(POS, 0)
    neg_count = counts.get(NEG, 0)
    if pos_count > neg_count:
        return POS_REVIEW
    elif neg_count > pos_count:
        return NEG_REVIEW
    else:
        return NONE


'''The main function is the entry point of the program.
When debugging, if you want to start from the very beginning,
start here.
'''


def main(argv):
    # The file that you will read should be passed as the argument to the program.
    # From python's point of view, it is the element number 1 in the array called argv.
    # argv is a special variable name. We don't define it ourselves; python knows about it.
    filename = argv[1]  # Place the first breakpoint here, when starting.

    # Now, we will call a function called cleanFileContents on the filename we were passed.
    # NB: We could have called the function directly on argv[1]; that would have the same effect.
    clean_text = cleanFileContents(filename)

    # Now, we will count how many times each word occurs in the review.
    # We are passing the text of the review, cleaned from punctuation, to the function called countTokens.
    # We assign the output of the function to a new variable we call tokens_with_counts.
    tokens_with_counts = countTokens(clean_text)

    # Call the simplistic prediction function on the obtained counts.
    # Store the output of the function in a new variable called "prediction".
    prediction = predictSimplistic(tokens_with_counts)

    # Finally, let's print out what we predicted. Note how we are calling the format()
    # function on the string we are printing out, and we are passing it two
    # arguments: the file name and our prediction. This is a convenient way of
    # printing out results. We will keep using it in the future.
    print("The prediction for file {} is {}".format(filename, prediction))


# The below code is needed so that this file can be used as a module.
# If we want to call our program from outside this window, in other words.
if __name__ == "__main__":
    main(sys.argv)