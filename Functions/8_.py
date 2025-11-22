# Write a function that counts vowels in a string
def count_vowels(v):
    vowel_count=0
    for char in v:
        if char in 'aeiouAEIOU':
            vowel_count+=1
    return vowel_count
vowels=input("Enter a string (like 'hello your name is john'): ")
print("Number of vowels in", vowels, "is:", count_vowels(vowels))