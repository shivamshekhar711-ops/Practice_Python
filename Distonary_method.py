#.keys()......................

student={
    "name":"Shiavm mishra",
    "dues":{
            "january":500,
            "february":900,
            "march":200,
        }
        
    }

print(student.keys())
print(list(student.keys()))

#.values...............................

student={
    "name":"Shiavm mishra",
    "dues":{
            "january":500,
            "february":900,
            "march":200,
        }
        
    }

print(student.values())
print(list(student.values()))


#.items...........................................

student={
    "name":"Shiavm mishra",
    "dues":{
            "january":500,
            "february":900,
            "march":200,
        }
        
    }

print(student.items())
print(list(student.items()))


#.get...........................................

student={
    "name":"Shiavm mishra",
    "dues":{
            "january":500,
            "february":900,
            "march":200,
        }
        
    }

print(student.get("name"))
print(list(student.get("dues")))


#.update................................................

student={
    "name":"Shiavm mishra",
    "dues":{
            "january":500,
            "february":900,
            "march":200,
        }
        
    }
student.update({"age":15})
print(student)




