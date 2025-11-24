# Find the second largest number in a list

num=[]
for i in range(5):
    n=int(input("Enter number{}: ".format(i+1)))
    num.append(n)
print(num)
num.sort()
print(num)
max1=num.remove(max(num))
max2=max(max)
print ("The second largest number is: ", max2)