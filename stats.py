def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def get_book_word_count(book):
    book_word_list = book.split()
    return len(book_word_list)
    
def get_letter_counts(book):
    letter_dict = {}
    word_list = book.split()
    for word in word_list:
        #letter_list = word.split()
        for letter in word:
            lower_letter = str(letter.lower())
            if (f"{lower_letter}") in letter_dict:
                letter_dict[f"{lower_letter}"] += 1
            else:
                letter_dict[f"{lower_letter}"] = int(1)
    return letter_dict