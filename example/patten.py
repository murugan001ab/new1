"""
get n number input from user
patten it works range
and print char of ascii value
"""
n= int(input())
k=n*2-3
for i in range(65,65+n):
    for j in range(1,k-1):
        print(end=" ")
    k=k-1
    for j in range(65,i+1):
        print(chr(j),end="")
    print("")