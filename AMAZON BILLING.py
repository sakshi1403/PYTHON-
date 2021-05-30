'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
Sentence = " Hey I am walking here I am walking here o captain my captain water water everywhere nor a drop to drink "
print("Sentence : ", Sentence, '\n')
sentence_list = Sentence.split()
print("Words are: ")
print(sentence_list, '\n')
sentence_set = set(sentence_list)
print("Unique words are : ")
print(sentence_set, '\n')
num_unique = len(sentence_set)
print("Number of unique words are :", num_unique, '\n')