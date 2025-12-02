# Ask the user to input 10 numbers.
# Create a list of unique numbers (remove duplicates without using set()).
# Find the max, min, sum, average, and second largest number.
# Create a dictionary where key = number and value = square of number.
# Print all even numbers from the list and count how many prime numbers exist.


def unique_list():
    numbers=[]
    for n in range(10):
        num=int(input("Enter number{}: ".format(n+1)))
        numbers.append(num)
        unique_numbers=[]
        for un in numbers:
            if un not in unique_numbers:
                unique_numbers.append(un)
    
    maximum = max(unique_numbers)
    minimum = min(unique_numbers)
    total = sum(unique_numbers)
    avg = total / len(unique_numbers)
    
    max1 = unique_numbers.remove(max(unique_numbers))
    max2=(max(unique_numbers))
    
    even = 0
    for e in unique_numbers:
        if e % 2 == 0:
            even+=1
            
    def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

    prime_count = sum(1 for num in unique_numbers if is_prime(num))
    print("The original list is: ", numbers, "\nThe list after removing duplicates is: ", unique_numbers)
    print(f"The maximum number is {maximum}\nminimum number is {minimum}\nsum of the list is {total}\navarage is {avg}\nsecond largest number is {max2}\ntotal even number is {even}\ntotal prime numbers are {prime_count}")

unique_list()