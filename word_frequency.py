import re


def word_frequency(pass_string):
    my_book = {}
    read_text = pass_string.split()
    for word in read_text:
        lower_it = word.lower()
        cleaned = re.sub("[^A-Za-z]", "", lower_it)
        if cleaned in my_book:
            my_book[cleaned] += 1
        else:
            my_book[cleaned] = my_book.get(cleaned, 0) + 1
    sort_my_book = sorted(my_book.items(), key=lambda x: x[1], reverse=True)[0:20]
    for word, count in sort_my_book:
        print(word, count)
    return my_book


with open("sample.txt") as raw_text:
    read_t = raw_text.read()
    word_frequency(read_t)
