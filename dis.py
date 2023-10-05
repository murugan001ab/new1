a=['python','maths','java','SE']
b=[10,20,30,40,50]
dis={}
def d(a,b):
    for x in range(len(a)):
            dis[a[x]]=b[x]

    print(dis)
d(a,b)
