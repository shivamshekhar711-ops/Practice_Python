list=[4,7,8,9,8]
for i in list:
    print(i)


#-------------------------------------

name=["shivam","samridh","ashutosh"]
for group in name:
    print(group)


#------------------------------------------------


name=("shivam","samridh","ashutosh")
for group in name:
    print(group)


#--------------------------------------------------

name="shiavm"
for char in name:
    print(char)


#---------------------------------------------------------

name="shiavm"
for char in name:
    if(char=="a"):
      print("a is found")
      break
    print(char)
else:
    print("end")