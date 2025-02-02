from itertools import count


def remove_whitespaces(x):
    return x.replace(" ", '').replace("\n",'')

def count_words(sentence, delimiter, count_only_alphabetic=False):
    my_list = list(map(lambda x: remove_whitespaces(x), sentence.split(delimiter)))
    # removes empty elements from the list
    my_list = [item for item in my_list if item != '']
    if count_only_alphabetic:
        indexes_to_remove = list()
        for i in range(len(my_list)):
            for character in my_list[i]:
                if character == my_list[i][0]:
                    continue
                if character == my_list[i][-1]:
                    continue
                if not character.isalpha():
                    indexes_to_remove.append(i)
        for index in sorted(indexes_to_remove, reverse=True):
            my_list.pop(index)
    return len(my_list)

print(count_words("1test;te2st;;;;test1", ";", True)) #2

