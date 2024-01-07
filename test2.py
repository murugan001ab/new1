import os
print("welcome to console Login ...!")
print("1.for create user")
print("2.for Login")
print("3.delete user")
opt=input("enter a option:")
try:
    if opt=='1':
        try:
            name=input("your name:")
            file=open(name,'w+')
            username=input('username:')
            file.writelines(username+'\n')
            file.write(input("password:")+'\n')
            file.write(input("email:")+'\n')    
            file.write(input("Mobile:")+'\n')
            print("user register success..!")
            os.rename(name,username)
            file.close()
        except IOError():
            print("cuuret input")
    elif opt=='2':
        try:
            word=[]
            print("welcome to login")
            username=input("enter a user name:")
            password=input("enter a password:")
            file=open(username,'r')
            for line in file:
                word+=line.split()
            if word[0]==username:
                if word[1]==password:
                    print("login success")
                else:
                    print("invalid password...!")
            else:
                print("Incurrect username...!")
            file.close()
        except IOError():
            print("cuuret input..!")
    elif opt=='3':
        name=input("enter user name:")
        os.remove(name)
        print(name,"deleted")
    else:
        print("enter a currect opt")
except IOError():
    print("enput error")