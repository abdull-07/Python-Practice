# Problem 2 — File & Text Analysis
# Ask the user to input a text file name.
# Count the number of lines, words, letters, and spaces.
# Print all words that start with a vowel.
# Save the analysis summary to a new file called summary.txt.
# Use functions wherever possible.

import os
# function that prints tasks 2,3.
def line_num():

    line_count = 0
    words_count = 0
    letters_count = 0
    spaces_count = 0
    vowel_words = []
    letters=[]
    
    file = input("Enter name of file to read that file: ")
    try:
        with open(file, 'r') as f:
            for line in f:
                line_count += 1
                word_in_line = line.split()
                words_count += len(word_in_line)
                
                for char in line:
                    if char.isalpha():
                        letters_count += 1
                    if char == " ":
                        spaces_count += 1
                        
                for word in word_in_line:
                    if word[0].lower() in 'aeiou':
                        vowel_words.append(word)
        print(f"Number of lines in '{file}': {line_count}")
        print(f"Number of words in '{file}': {words_count}")
        print(f"Number of letters in '{file}': {letters_count}")
        print(f"Number of spaces in '{file}': {spaces_count}")
        print(f"Words starting with vowels: {vowel_words}")
        with open("summary.txt", 'w') as f:
            f.write(f"Number of lines in '{file}': {line_count}\nNumber of words in '{file}': {words_count}\nNumber of letters in '{file}': {letters_count}\nNumber of spaces in '{file}': {spaces_count}\nWords starting with vowels: {vowel_words}")
    except FileNotFoundError:
        print(f"Error: File {file} not found")
    except Exception as e:
        print("An unexpected error occoure")


def read_file():
    line_num()
read_file()
