# 1. Write a program to check if there is a vowel in a string.

names = input("enter: ") #Programming
vowels = "aeiouAEIOU"
count = 0

for name in names:
    for i in vowels:
        if i == name:
            count+=1

if count >= 1: 
    print("The string contains a vowel.")
else:
    print("The string does not contain any vowel.")


#2. Write a program where user will give height(height) and weight(kg) and then BMI will be calculated.

inp = map(float, input().split())
h, w = inp
h = float(h)
w = int(w)
BMI = w / (h * h)
print(f"BMI: {BMI:.2f}")

if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25.0:
    print("Normal weight")
elif 25.0 <= BMI < 30.0:
    print("Overweight")
else:
    print("Obese")
