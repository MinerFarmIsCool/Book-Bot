from stats import get_book_text, get_book_word_count, get_letter_counts
from formatter import print_the_formatted_book_stuff
import sys





def main():
    how_many_args = len(sys.argv)
    if how_many_args != 2:
        print("Usage: python3 main.py <path_to_book>")
        print("Invalid argument count")
        sys.exit(1)
    try:
        book_path = sys.argv[1]
        print_the_formatted_book_stuff(book_path)
    except:
        print("Usage: python3 main.py <path_to_book>")
        print("Invalid path to book")
        sys.exit(2)


    


main()