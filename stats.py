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
    letter_dict = format_letter_counts(letter_dict)
    return letter_dict

def format_letter_counts(letter_dict):
    letter_list = []
    for letter in letter_dict:
        if letter.isalpha():
            count = letter_dict[letter]
            meow_dict = {"char": letter, "count": count}
            letter_list.append(meow_dict)

    letter_list.sort(reverse=True, key=get_sort)
    return letter_list

def get_sort(dicty):
    return dicty["count"]

def get_stats(filepath):
    book = get_book_text(filepath)
    word_count = get_book_word_count(book)
    letter_counts = get_letter_counts(book)
    return book, word_count, letter_counts