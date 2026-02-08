a=[2,6,9]
b=[2,9,7,]
c=b

print(a is b)
print(b is a)
print(b is c)
print(a is not b)
print(c is not b)



x=int(input("enter 1st number"))
y=int(input("enter 2nd number"))
z=int(input("enter 3rd number"))

l=x is y is z
print(l)

m=x is y is not z
print(m)
