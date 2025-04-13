#1. Write a program where you will be given an array arr[] of size N and an integer P. Find the triplet in the array which sums up to the given integer P.

N = int(input("Enter: "))

inp = map(int, input("kk:").split())
arr = list(inp) # 12 3 4 1 6 9

target = int(input("Enter target: "))
count = 0


for x in arr[0:]: 
    for y in arr[1:]:
        for z in arr[2:]:
            if x + y + z == target:
                count+=1
            if count == 1:
                print("Triplet found:", x, y, z)




# print(x)