# Write a function that prints the square of each number in a list
def squire(num_list):
    for num in num_list:
        print("The squire of", num," is ",num**2)
#Example
list=[]
for i in range(10):
    n=int(input(f"Enter number {i+1} in list: "))
    list.append(n)
squire(list)