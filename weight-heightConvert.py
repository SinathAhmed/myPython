print("what is your name?")
name = input()
print(f"Hello {name}. I am going to convert your weight and height to metric system.")
print("Now, what do you want to convert? (W for weight, H for height)")
choice = input()

if choice == "W":
    print("Enter your weight")
    weight = float(input())
    print("Kilogram or pound? (K for kilogram, P for pound)")
    unit = input()
    if unit == "K":
        print(f"your weight in pound is {weight * 2.20462}")
    elif unit == "P":
        print(f"your weight in kilogram is {weight / 2.20462}")
    else:
        print("Mathay somossha? chokhe dekha jay na ki chaisi ??")
        # print("Invalid unit. Please enter K for kilogram or P for pound.")
        # exit()

elif choice == "H":
    print("Enter your height")
    height = float(input())
    print("Centimeter or feet? (C for centimeter, F for Feet)")
    unit = input()
    if unit == "C":
        print(f"your height in feet is {height * 0.0328084}")
    elif unit == "F":
        print(f"your height in centimeter is {height / 0.0328084}")
    else:
        print("Mathay somossha? chokhe dekha jay na ki chaisi ??")
        # print("Invalid unit. Please enter C for centimeter or F for feet.")
        # exit()

else:
    print("Mathay somossha? chokhe dekha jay na ki chaisi ??")
    # print("Invalid choice. Please enter W for weight or H for height.")
    # exit()