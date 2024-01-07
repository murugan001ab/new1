import re
a='good morning ! 1234 @'
alpha=0
num=0
sp=0
Alp=re.findall('[a-z]',a)
num=re.findall('[0-9]',a)
print(len(Alp))
print(len(num))
print(len())
'''
alb=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num1=['1','2','3','4','5','6','7','8','9','0']
for word in a:
    if word in alb:
        alpha+=1
    elif word in num1:
        num+=1
    else:
        sp+=1
        ''''''
print('alpha=',alpha)
print('num=',num)
print('symbol=',sp)
'''