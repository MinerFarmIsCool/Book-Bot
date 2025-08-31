from stats import get_book_text, get_book_word_count


def main():
    frankenstein_text = get_book_text("books/frankenstein.txt")
    frankenstein_word_count = get_book_word_count(frankenstein_text)
    print(f"{frankenstein_word_count} words found in the document")

main()