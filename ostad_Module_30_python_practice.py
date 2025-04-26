#1 Write a program that checks if a year entered by the user is a leap year or not.

# inp = int(input())

# if (inp % 4 == 0 and inp % 100 != 0) or (inp % 400 == 0):
#     print(f"{inp} is a leap year.")
# else:
#     print(f"{inp} is not a leap year.")

#2 Write a program to calculate distance between two points.


inp1 = map(int, input().split())
inp2 = map(int, input().split())

a, b = inp1
c, d = inp2

distance = ((c - a) ** 2 + (d - b) ** 2) ** 0.5
print(f"The distance between the two points is: {distance:.2f}")


#3 Write a program that checks if a number entered by the user is positive, negative, or zero.

# inp = int(input())
 
# if inp > 0:
#     print(f"{inp} is a positive number.")
# elif inp < 0:
#     print(f"{inp} is a negative number.")
# else:
#     print("The number is zero.")

#4 Write a program that swaps the values of two variables.

# inp = map(int, input().split()) 
# a, b = inp
# temp = 0
# print(f"Before swapping: num1 = {a}, num2 = {b}")

# temp = a
# a = b
# b = temp

# print(f"After swapping: num1 = {a}, num2 = {b}")
