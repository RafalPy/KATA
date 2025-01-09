

def count_words(sentence, delimiter):
    my_list = sentence.split(delimiter)
    counter = 0
    for i in range(len(my_list)):
        if len(my_list[i]) != 0:
        counter +=1



    return counter

print(count_words("test;test;test", ";")) #3
print(count_words("test;test;;test", ";")) #3
print(count_words("test;test;;;;test", ";")) #3
print(count_words("test;test;test", ".")) #1