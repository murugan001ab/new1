"""
input
split
+alpha
then join
print

"""
str=input()
output=""
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in str:
    space=" "
    if i==space:
        output+=" "
    else:
        idx=alpha.index(i)
        if idx==25:
            output+='b'
        elif idx==24:
            output+='a'
        else:    
            inc=idx+2
            output+=alpha[inc]
print(output)

