# if elif else
age=int(input("Enter your age:"))
if age>=18:
    print("You are eligible for vote")
    print("ELEIGIBLE FOR LICENENCE")   




light=input("enter your light") 
if (light=="green"):
    print("Stop")
elif (light=="red"):
    print("go")
elif (light=="yellow"):
    print("wait")



age=int(input("Enter your age:"))
if age>=18:
    print("You are eligible for vote")
    print("ELEIGIBLE FOR LICENENCE")

else:
    print("not eligible for vote") 
    print("not eligible for driving licinence") 


marks=int(input("enter your marks"))
if(marks>=300):
    print("First Division")
elif(marks>=225):
    print("Second Division")
elif(marks>=150):
    print("third Division")
else:
    print("fail")



x=int(input("enter your marks of math"))
if(x>=90):
    print("grade A")
elif(x>=50):
    print("grade B")
elif(x>=40):
    print("grade C")
else:
    print("grade d")
    

# nested statememnt


a = int(input("Enter a number: "))

if a > 0:
    if a % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Number is Negative or Zero")
