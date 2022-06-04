import sys
import pandas as pd


def countTokens(text):
    token_counts = {}
    tokens = text.split(' ')
    for word in tokens:
        if word not in token_counts:
            token_counts[word] = 0
        token_counts[word] += 1
    updated_token_counts = sorted(token_counts, reverse=True)
    problem_solver = {}
    for index in range(len(updated_token_counts) - 2):
        if index % 2:
            problem_solver[updated_token_counts[index]] = updated_token_counts[index + 2]
    for index in range(len(updated_token_counts) - 2):
        if not index % 2:
            problem_solver[updated_token_counts[index]] = updated_token_counts[index + 2]
    return problem_solver


def largest_counts(data):
    pos_train_data = data[:12500]
    neg_train_data = data[12500:25000]

    train_counts_pos_original = countTokens(pos_train_data["review"].str.cat())
    train_counts_pos_cleaned = countTokens(
        pos_train_data["cleaned_review"].str.cat())
    train_counts_pos_lowercased = countTokens(
        pos_train_data["lowercased"].str.cat())
    train_counts_pos_no_stop = countTokens(
        pos_train_data["no stopwords"].str.cat())
    train_counts_pos_lemmatized = countTokens(
        pos_train_data["lemmatized"].str.cat())
    train_counts_neg_original = countTokens(neg_train_data["review"].str.cat())
    train_counts_neg_cleaned = countTokens(
        neg_train_data["cleaned_review"].str.cat())
    train_counts_neg_lowercased = countTokens(
        neg_train_data["lowercased"].str.cat())
    train_counts_neg_no_stop = countTokens(
        neg_train_data["no stopwords"].str.cat())
    train_counts_neg_lemmatized = countTokens(
        neg_train_data["lemmatized"].str.cat())

    with open('counts.txt', 'w') as f:
        f.write('Original POS reviews:\n')
        for k, v in list(train_counts_pos_original.items())[:20]:
            f.write('{}\t{}\n'.format(k, v))
        f.write('Cleaned POS reviews:\n')
        for k, v in list(train_counts_pos_cleaned.items())[:20]:
            f.write('{}\t{}\n'.format(k, v))
        f.write('Lowercased POS reviews:\n')
        for k, v in list(train_counts_pos_lowercased.items())[:20]:
            f.write('{}\t{}\n'.format(k, v))
        f.write('No stopwords POS reviews:\n')
        for k, v in list(train_counts_pos_no_stop.items())[:20]:
            f.write('{}\t{}\n'.format(k, v))
        f.write('Lemmatized POS reviews:\n')
        for k, v in list(train_counts_pos_lemmatized.items())[:20]:
            f.write('{}\t{}\n'.format(k, v))
        f.write('Original NEG reviews:\n')
        for k, v in list(train_counts_neg_original.items())[:20]:
            f.write('{}\t{}\n'.format(k, v))
        f.write('Cleaned NEG reviews:\n')
        for k, v in list(train_counts_neg_cleaned.items())[:20]:
            f.write('{}\t{}\n'.format(k, v))
        f.write('Lowercased NEG reviews:\n')
        for k, v in list(train_counts_neg_lowercased.items())[:20]:
            f.write('{}\t{}\n'.format(k, v))
        f.write('No stopwords NEG reviews:\n')
        for k, v in list(train_counts_neg_no_stop.items())[:20]:
            f.write('{}\t{}\n'.format(k, v))
        f.write('Lemmatized NEG reviews:\n')
        for k, v in list(train_counts_neg_lemmatized.items())[:20]:
            f.write('{}\t{}\n'.format(k, v))

    # TODO: Copy the output of the above print statements
    #  into your document/report, or otherwise create a table/visualization for these counts.


def main(argv):
    data = pd.read_csv(argv[1], index_col=[0])
    #print(data.head())
    largest_counts(data)


if __name__ == "__main__":
    main(sys.argv)
