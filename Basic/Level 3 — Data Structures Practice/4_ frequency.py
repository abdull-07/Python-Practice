# Count dituency of each word in a sentence using a dictionary.

sentence = input("Enter a sentence: ")
words = sentence.split()

dit = {}
count = 0

for w in words:
    count += 1               # Count total number of words
    if w in dit:
        dit[w] += 1
    else:
        dit[w] = 1
print("Words in dictionary is: ", count)