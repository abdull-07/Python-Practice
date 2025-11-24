# Merge two sorted lists into one sorted list.
list1=int(input("Enter the number of elements for List 1: "))
for i in range(5):
    if i==0:
        list_1=[]
        element=int(input("Enter element for list 1: ".format(i+1)))
        list_1.append(element)
    else:
        element=int(input("Enter element for list 1: ".format(i+1)))
        list_1.append(element)
        
list2=int(input("Enter the number of elements of list 2: "))
for i in range(5):
    if i==0:
        list_2=[]
        element=int(input("Enter element for list 1: ".format(i+1)))
        list_2.append(element)
    else:
        element=int(input("Enter element for list 1: ".format(i+1)))
        list_2.append(element)

list3=list_1+list_2
list3.sort()    
print("The first list is: ",list_1, "\nThe second list is: ",list_2, "\nThe Merge list is: ",list3)