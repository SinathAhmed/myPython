#1 Write a program to find the remainder of two numbers (modulo operation).

nums = map(int, input("Enter two numbers separated by space: ").split())
a, b = nums

c = int(a % b)

print(c)


#2 Write a program to find the quotient of two numbers (integer division).

nums = map(int, input("Enter two numbers separated by space: ").split())
a, b = nums

c = int(a // b) 
print(c)