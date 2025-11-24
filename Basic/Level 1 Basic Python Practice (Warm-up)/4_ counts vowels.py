# Create a program that counts how many vowels are in a string.
vowels=input("Enter a string (like 'hello your name is john'): ")
vowel_count=0
for char in vowels:
    if char in 'aeiouAEIOU':
        vowel_count+=1
print("Number of vowels in", vowels, "is:", vowel_count)