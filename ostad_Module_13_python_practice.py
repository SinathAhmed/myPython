#1. Write a program where you will be given an array arr[] of size N and an integer P. Find the triplet in the array which sums up to the given integer P.

# def find_triplet(arr, target):
#     n = len(arr)
#     for i in range(n - 2):
#         for j in range(i + 1, n - 1):
#             for k in range(j + 1, n):
#                 if arr[i] + arr[j] + arr[k] == target:
#                     return arr[i], arr[j], arr[k]
#     return None

# print(find_triplet([12, 3, 4, 1, 6, 9], 24)) # (12, 3, 9)



# N = int(input("Enter: "))
"""
inp = map(int, input("kk:").split())
arr = list(inp) # 12 3 4 1 6 9

target = int(input("Enter target: "))
count = 0


for x in arr[0:]: 
    for y in arr[1:]:
        for z in arr[2:]:
            if x + y + z == target:
                count+=1
                break

    if count == 1:
        print("Triplet found:", x, y, z)



# print(x)"""