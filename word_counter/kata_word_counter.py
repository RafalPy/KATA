
def count_words(sentence, delimiter):
    my_list = sentence.split(delimiter)
    counter_1 = 0
    for i in range(len(my_list)):
        counter_2 = 0
        for character in my_list[i]:
            if character.isspace():
                counter_2 += 1
            if len(my_list[i]) == counter_2 & counter_2 !=0:
                counter_1 -=1
        if len(my_list[i]) != 0:
            counter_1 +=1

    return counter_1

#function counts only alphabetic words but also those ending or starting with not an alphabetic character
def count_words_alphabetic(sentence, delimiter, count_only_alphabetic=True):
    my_list = sentence.split(delimiter)
    new_list2 = my_list
    indexes_to_remove = []
    if count_only_alphabetic:
        for i in range(len(new_list2)):
            for character in new_list2[i]:
                if character == new_list2[i][0]:
                    continue
                if character == new_list2[i][-1]:
                    continue
                if not character.isalpha():
                    indexes_to_remove.append(i)
        decreaser = 0
        for index in indexes_to_remove:
            if decreaser != 0:
                for index in indexes_to_remove:
                    index -= 1
            new_list2.pop(index)
            decreaser += 1

    for word in my_list:
        pass
    counter_1 = 0
    for i in range(len(my_list)):
        counter_2 = 0
        for character in my_list[i]:
            if character.isspace():
                counter_2 += 1
            if len(my_list[i]) == counter_2 & counter_2 != 0:
                counter_1 -= 1
        if len(my_list[i]) != 0:
            counter_1 += 1
    return counter_1

print(count_words_alphabetic("1test;te1t;test;te3t", ";"))



