# Take a sentence as input and count:
# Words
# Letters
# Spaces
# lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


sentence=input("Enter a sentence: ")
words=sentence.split()
num_words=len(words)
num_letters=len(sentence.replace(" ",""))
num_spaces=sentence.count(" ")
print(" The sentence is: ", sentence, "\n Number of words: ", num_words, "\n Number of letters: ", num_letters, "\n Number of spaces: ", num_spaces)