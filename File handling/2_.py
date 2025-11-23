# Write a program to read a file and print all words that start with a vowel.
open_file = open("sample.txt", 'r')
vowel_words = []
for line in open_file:
    words = line.split()
    for word in words:
        if word[0].lower() in 'aeiou':
            vowel_words.append(word)
open_file.close()
print("Words that start with a vowal: ", vowel_words)