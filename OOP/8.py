# Use lambda + filter to keep even numbers only

even = list(filter(lambda x: x%2 == 0, range(1,101)))
print(even)

# here is also for odd numbers
odd = list(filter(lambda x: x%2 != 0, range(1,101)))
print(odd)