# Problem 4 — Nested & Comprehensions
# Ask the user for 5 lists, each with 3 integers.
# Merge them into a single flat list using a nested loop.
# Generate a list of squares of all numbers in the merged list using list comprehension.
# Create a set of unique numbers from the squares using set comprehension.
# Print the dictionary where key = number, value = its square.

def get_list():
    all_list = []
    for i in range(5):
        nums = input(f"Enter 3 integers for list {i+1} sperated by space: ")
        lst = list(map(int, nums.split()))
        all_list.append(lst)
    return all_list

def merg_list(nested_list):
    flat_list = []
    for sublist in nested_list:
        for n in sublist:
            flat_list.append(n)
    return flat_list

def gen_sqr(flat_list):
    sqr_list= []
    for n in flat_list:
        list = n*n
        sqr_list.append(list)
    return sqr_list

def uniq_num(flat_list):
    uniqe_list = []
    for u in flat_list:
        if u not in uniqe_list:
            uniqe_list.append(u)
    return uniqe_list

def gen_dict(flat_list):
    uniqe_list = []
    for u in flat_list:
        if u not in uniqe_list:
            uniqe_list.append(u)
    print(f"The unique list is: {uniqe_list}")

    for value, sqr in enumerate(uniqe_list, start=uniqe_list[0]):
        print(f"{value}: {sqr*sqr}")


def main():
    all_list = get_list()
    print(f"The final list is: {all_list}")
    
    flat_list = merg_list(all_list)
    print(f"The single flate list is: {flat_list}")
    
    sqr_list = gen_sqr(flat_list)
    print(f"The sqre list of flat list is: {sqr_list}")
    
    uniqe_list = uniq_num(flat_list)
    print(f"The unique list is: {uniqe_list}")

main()