#8 Create a list of squares of numbers from 1 to 20 using a list comprehension.\

def gen_squrs():
    squres = [x*x for x in range(1,21)]
    return squres
print(gen_squrs())


# 9 Create a dictionary from a list of numbers, where key = number, value = square.
def gen_squrs():
    squres = [x*x for x in range(1,21)]
    return squres

def gen_dict():
    numbers = list(range(1,21))
    squars = gen_squrs()
    num_dict = {numbers[i] : squars[i] for i in range(len(numbers))}
    return num_dict
print(gen_dict())