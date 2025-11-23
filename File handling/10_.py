# Create a set of unique letters from a string using a set comprehension
def uniq_let(str):
    # open_file = open("sample.txt", "r")
    # str = open_file.read()
    letters = {char for char in str if char.isalpha()}
    return letters
print(uniq_let('Hello, world!'))