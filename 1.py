# print("Abdullah")

# num =int( input("Enter a number: "))
# if((num)%2==0):
#     print("You Entered:", num, "which is Even Number")
# else:
#     print("You Entered:", num, "which is Odd Number")

# print("Thank You!")



# num1 =int( input("Enter a first number: "))
# num2 =int( input("Enter a second number: "))
# sig=input("enter a operator:")

# if sig=='+':
#     print("The addition is:", num1+num2)
# elif sig=='-':
#     print("The addition is:", num1-num2)
# elif sig=='*':
#     print("The addition is:", num1*num2)
# elif sig=='/':
#     print("The addition is:", num1/num2)
# else:
#     print("Invalid operator")

# print("Thank You!")


# # Multiplication table generator
# mun1 = int(input("Enter a number for Table:"))
# for i in range(1,11):
#     print(mun1, 'x', i, '=', mun1*i)

# # Find max/min number in a lis
# num = [12, 45, 7, 23, 89, 4]
# print("The list is:", num)
# if not num:
#     print("The list is empty.")
# else:
#     max=num[0]
#     min=num[0]
#     for num in num:
#         if num>max:
#             max=num
#         if num<min:
#             min=num
# print("The maximum number is:", max)
# print("The minimum number is:", min)


# numbers = [15, 30, 47, 82, 95]
# def lesser(numbers):
#    return numbers < 50

# small = list(map(lesser, numbers))
# print(small)

# names = ["Anna", "Natasha", "Mike"]
# names.insert(2, "Xi")
# print(names)

# sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
# for x in sample_dict:
#     print(x)

# def recursion(num):
#     print(num)
#     next = num - 3
#     if next > 1:
#         recursion(next)

# recursion(11)


# def bigo(numbers):
#     for i in numbers:
#         print(numbers)

# bigo([1, 7, 13, 19])

# def d():
#     color = "green"
#     def e():
#         nonlocal color
#         color = "yellow"
#     e()
#     print("Color: " + color)
#     color = "red"
# color = "blue"
# d()  


# num = 9
# class Car:
#     num = 5
#     bathrooms = 2
# def cost_evaluation(num):
#     num = 10
#     return num

# class Bike():
#     num = 11

# cost_evaluation(num)
# car = Car()
# bike = Bike()
# car.num = 7
# Car.num = 2
# print(num) 



# class A:
#    def a(self):
#        return "Function inside A"

# class B:
#    def a(self):
#        return "Function inside B"

# class C:
#    pass

# class D(C, A, B):
#    pass

# d = D()
# print(d.a())