# Write a program that checks if a number entered by the user is positive, negative, or zero.

inp = int(input())
 
if inp > 0:
    print(f"{inp} is a positive number.")
elif inp < 0:
    print(f"{inp} is a negative number.")
else:
    print("The number is zero.")