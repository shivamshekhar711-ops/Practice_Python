i=0
while i<=20:
    print(i)
    if(i==10):
        break
    i+=1


#-----------------------------------



nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)

x = int(input("enter a number"))
i = 0

while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx", i)
        break
    else:
        print("finding..",i)
    i += 1



