# Convert a loop into list comprehension (e.g., squares of numbers)

lst = []
squares = []
for i in range(1, 21):
    lst.append(i)
    squares.append(i*i)
print(f"{lst}\n{squares}")

squares = [i*i for i in range(1, 21)]
print(squares)