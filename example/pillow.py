"""
get  person and time
then print index were is  time
"""
person=int(input("person"))
time=int(input("time"))
list=[]
list1=[]
for x in range(1,person+1):
    list.append(x)
for y in list:
    if(time<person):
        print(y,'->',end="")
    else:
        print(y, '->', end="")
        list1=list[::-1]
    for z in list1:
        print(z,'->',end="")
