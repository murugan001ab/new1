"""
get input from user
convert to list then
pass to loop and calclude pass or fail
"""
marks=input("enter a marks").split(",")
print(marks)
for x in marks:
    if x>='35':
        print("pass",end=",")
    else:
        print("fail",end=",")