import pandas as pd
import sys

from Newa4 import calculations

def main(argv):
    data = pd.read_csv('my_imdb_expanded.csv')

    nb_original = calculations(data['review'])
    nb_cleaned = calculations(data['cleaned_review'])
    nb_lowercase = calculations(data['lowercased'])
    nb_no_stop = calculations(data['no stopwords'])
    nb_lemmatized = calculations(data['lemmatized'])

if __name__ == "__main__":
    main(sys.argv)
