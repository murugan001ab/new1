file3=open('new1.txt','r')
file4=open('new','a+')
word=input("enter word:")
total=0
for lines in file3:
    total+=lines.count(word)
print(total)