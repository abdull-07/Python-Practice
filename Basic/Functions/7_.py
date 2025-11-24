# Write a function that returns both the sum and average of a list.

def sum_all(*arg):
    total=0
    for a in arg:
        total+=a
    avg=total/len(arg)
    return total, avg
list=[]
for i in range(5):
    n=input(f"Enter number {i+1} in list: ")
    list.append(int(n))
print("The sum of all numbers is: ", sum_all(*list)[0], "and the average is: ", sum_all(*list)[1])