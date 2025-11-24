# Check if a number is a prime number.
num=int(input("Enter a number: "))
is_prime=True
if num<=1:
    is_prime=False
    print(num, "is a not prime number.")
else:
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            is_prime=False
            print(num, "is a not prime number.")
            break
if is_prime:
    print(num, "is a prime number.")