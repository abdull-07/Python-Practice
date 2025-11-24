#7.2 Create your own module with a function greet(name) and import it in another file.
# main file

# greet_module is the module file

from greet_module import greet
name=input("Enter yur name: ")
print(greet(name))