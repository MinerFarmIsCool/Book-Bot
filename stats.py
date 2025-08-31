def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def get_book_word_count(book):
    book_word_list = book.split()
    return len(book_word_list)
    