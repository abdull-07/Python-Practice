# Write a function is_even(n) that returns True if a number is even.
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
num = int(input("Enter a number: "))
is_even(num)
print(is_even(num))