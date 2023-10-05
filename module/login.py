import oprations as op
username="hacker"
password="muru2466"
def login():
    iusername=input("enter username")
    ipassword=input("enter password")
    if(iusername==username):
        if(ipassword==password):
            return True
        else:
            print("incorrect posword")
    else:
        print("user name incorrect")
