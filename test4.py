def leter(str):
    try:
        output=""                               #declare empty string
        for j in range(len(str)):               #iterate length of str
            output+=str[j].upper()+str[j]*j+'-' #fist leter is upper use upper() #str[j] mean str[0] value is m like all                                     
        print(output)                           #print output
    except Exception as e:
        print(e)         

leter('murugan')              
#if alter use zip() 
"""
for i,j in zip(str,range(len(str))):
    output+=i.upper()+i*j+'-'
print(output)
"""