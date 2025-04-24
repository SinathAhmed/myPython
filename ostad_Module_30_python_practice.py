#3 Write a program that checks if a number entered by the user is positive, negative, or zero.

# inp = int(input())
 
# if inp > 0:
#     print(f"{inp} is a positive number.")
# elif inp < 0:
#     print(f"{inp} is a negative number.")
# else:
#     print("The number is zero.")

#4 Write a program that swaps the values of two variables.

inp = map(int, input().split()) 
a, b = inp
temp = 0
print(f"Before swapping: num1 = {a}, num2 = {b}")

temp = a
a = b
b = temp

print(f"After swapping: num1 = {a}, num2 = {b}")