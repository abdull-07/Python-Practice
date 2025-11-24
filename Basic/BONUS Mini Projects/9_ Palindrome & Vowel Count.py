# Problem 7 — Palindrome & Vowel Count
# Ask the user for a sentence.
# Count number of vowels and number of words starting/ending with a vowel.
# Check if each word is a palindrome and print results.
# Store palindrome words in a list and print the total count.


vowel_count = 0
start_vowel_count = 0
end_vowel_count = 0
palindrome = []

str = input("Enter a sentence: ")
print(f"You enter: {str}")

for w in str:
    if w in 'aeiou':
        vowel_count += 1

words = str.split()
print(words)
for  word in words:
    word_clean = word.lower().strip(".,!?")
    if word_clean[0].lower() in 'aeiou':
            start_vowel_count += 1
    if word_clean[-1].lower() in 'aeiou':
            end_vowel_count += 1
    if word_clean == word_clean[::-1]:
        palindrome.append(word)




print(f"The number of vowels in the sentence is: {vowel_count}")
print(f"The number of words starting with a vowel: {start_vowel_count}")
print(f"The number of words ending with a vowel: {end_vowel_count}")
print(f"Palindrome words: {palindrome}")
print(f"Total number of palindrome words: {len(palindrome)}")