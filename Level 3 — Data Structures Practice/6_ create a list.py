#Create a list of fruits and:
# Add a fruit
# Remove a fruit
# Update a fruit
# Search if a fruit exists


furites=[]
for f in range(5):
    furite=input("Enter the name of furites: ")
    furites.append(furite)

print(furites)
f1=input("Enter another name of furite that not in list: ")
furites.append(f1)
print("The updated list of furites is",furites)
f1=input("Enter another name of furite from the list: ")
furites.remove(f1)
print("The updated list of furites is",furites)
f1=input("Enter the furite name to update: ")
idx=int(input("Enter the idx to update the furote name: "))
furites[idx]=f1
print("The updated list of furites is",furites)

search=input("Enter any fruite to search for list: ")
if search in furites:
      idx=furites.index(search)
      print(search, "is available in the list at idx: ", idx)
else:
    print(search, "is NOT in the list.")