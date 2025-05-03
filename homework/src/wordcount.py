# obtain a list of files in the input directory

from ._internals.count_word_occurrences import count_word_occurrences
from ._internals.extract_words import extract_words
from ._internals.normalize_lines import normalize_lines
from ._internals.read_input_files import read_input_files
from ._internals.write_count_words import write_count_words


def main():

    input_folder = "data/input"
    output_folder = "data/output"

    all_lines = read_input_files(input_folder)
    all_lines = normalize_lines(all_lines)
    words = extract_words(all_lines)
    counter = count_word_occurrences(words)
    write_count_words(counter, output_folder)


if __name__ == "__main__":
    main()
