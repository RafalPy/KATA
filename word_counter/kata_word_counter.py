
def count_words(sentence, delimiter):
    my_list = sentence.split(delimiter)
    print(my_list)
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

print(count_words("test;test; ;", ";"))  #2 expected, single space test
print(count_words("test;test;    ;test", ";")) #3 expected, multiple spaces test
print(count_words("test;test;   ;test", ";"))  #3 expected, tab test
print(count_words("test;test; test;test", ";"))  #4 expected, word with space test


