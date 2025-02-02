from itertools import count
from operator import index


def remove_whitespaces(x):
    return x.replace(" ", '').replace("\n",'')

def count_words(sentence, delimiter, count_only_alphabetic=False):
    my_list = list(map(lambda x: remove_whitespaces(x), sentence.split(delimiter)))
    # removes empty elements from the list
    my_list = [item for item in my_list if item != '']
    if count_only_alphabetic:
        non_alpha_word_indices = [my_list.index(word) for word in my_list for character in word if not character.isalpha() and word.index(character) != 0 and word.index(character) != (len(word) -1)]
        for index in sorted(non_alpha_word_indices, reverse=True):
            my_list.pop(index)
    return len(my_list)


print(count_words("1test;te2st; ;;;test1", ";", True)) #2

