from stats import get_stats

def print_the_formatted_book_stuff(filepath):
    book, book_word_count, book_letter_count = get_stats(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    for dict in book_letter_count:
        print(f"{dict['char']}: {dict['count']}")