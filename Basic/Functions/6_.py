# Write a function that accepts any number of arguments (*args) and returns their sum.
def sum_all(*arg):
    t=0
    for a in arg:
        t+=a
    return t
list=[]
for i in range(5):
    n=input(f"Enter number {i+1} in list: ")
    list.append(int(n))
print("The sum of all numbers is: ", sum_all(*list))