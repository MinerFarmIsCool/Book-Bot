

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def get_book_word_count(book):
    book_word_list = book.split()
    return len(book_word_list)
    
def main():
    frankenstein_text = get_book_text("books/frankenstein.txt")
    frankenstein_word_count = get_book_word_count(frankenstein_text)
    print(f"{frankenstein_word_count} words found in the document")

main()