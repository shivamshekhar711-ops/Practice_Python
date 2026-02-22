a="hello"
while True:
    print(a)


i=1
while i<=5:
    print("hello")
    i+=1




i=1
while i<=5:
    print(i)
    i+=1

    



i=5
while i>=1:
    print(i)
    i-=1





#---------------------------------------------------------------

count=1
while count<=5:
    print("hello")
    count=count+1

#------------------------------------------------------

i=5
while i<=9:
    print("jay hind")
    i=i+1

#--------------------------------------------------------

i=1
while i<=5:
    print("jay hind")
    i+=1
    
# #------------------------------------------------------

i=1
while i<=50:
    print("jay hind" ,i)
    i+=1
    
#------------------------------------------------

num=1
while num<=10:
    print(num)
    num+=1


# #------------------------------------------------------

i=10
while i>=1:
    print(i)
    i-=1


# #----------------------------------------------

i=5
while i<=6:
    print(i)
    i-=1


#-------------------------------------------
#  Q.(1-100) print

i=1
while i<=100:
    print(i)
    i+=1

#   Q.(100-1)print


i=100
while i>=1:
    print(i)
    i-=1


#   Q.print any number table

n=int(input("enter a number:"))
i=1
while i<=10:
    print(n*i)
    i+=1

#   Q.print 1,4,9,16,25,36,49,64,81,100 by loop

i=1
while i<=10:
    print(i*i)
    i+=1

#    Q.[1,5,1,4,7,2,9,] print loop method

num=[1,5,1,4,7,2,9,]
index=0
while index<len(num):
    print(num[index])
    index+=1

      #or,

num=[1,5,1,4,7,2,9,]
index=0
while index<=6:
    print(num[index])
    index+=1


#    Q. Found at tuple (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)


nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)

x = int(input("enter a number"))
i = 0

while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx", i)
    else:
        print("finding..")
    i += 1

