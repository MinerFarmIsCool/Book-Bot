from stats import get_book_text, get_book_word_count, get_letter_counts
from formatter import print_the_formatted_stuff


def not_main():
    frankenstein_text = get_book_text("books/frankenstein.txt")
    frankenstein_word_count = get_book_word_count(frankenstein_text)
    print(f"{frankenstein_word_count} words found in the document")
    frankenstein_letter_dict = get_letter_counts(frankenstein_text)
    print(frankenstein_letter_dict)

def main():
    print_the_formatted_stuff("books/frankenstein.txt")


main()