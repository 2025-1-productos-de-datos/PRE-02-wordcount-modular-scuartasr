# obtain a list of files in the input directory

from homework.src._internals.normalize_lines import normalize_lines

from ._internals.count_word_occurrences import count_word_occurrences
from ._internals.extract_words import extract_words
from ._internals.read_input_files import read_input_files
from ._internals.write_count_words import write_count_words


def main():

    ## read all lines
    all_lines = read_input_files()

    ## preprocess lines
    all_lines = normalize_lines(all_lines)

    ## split in words
    words = extract_words(all_lines)

    ## count words
    counter = count_word_occurrences(words)

    # count the frequency of the words in the files in the input directory
    # counter = {}
    # for filename in input_file_list:
    #     with open("data/input/" + filename) as f:
    #         for l in f:
    #             for w in l.split():
    #                 w = w.lower().strip(",.!?")
    #                 counter[w] = counter.get(w, 0) + 1

    ##
    write_count_words(counter)


if __name__ == "__main__":
    main()
