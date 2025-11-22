# Count how many times a number repeats in a list

num=[1,2,3,4,55,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,1,6,7,8,5,4,8,4,9,7,0,0,12,34,56,23,12,65,98,56,34,32,12,67,89,56,65,3443,23,212,87,89]
n=int(input("Enter a number to check how many times it repeats in the list: "))
c=0
for i in num:
    if i==n:
        c+=1
print("The number", n, "repeats",c,"times in the list.")
