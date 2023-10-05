if __name__ == '__main__':
    list1=[]
    temscore=[]
    result=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])
        temscore.append(score)
    temscore=list(set(temscore))
    temscore.sort()
    seclo=temscore[1]
    for x in range(len(list1)):
        if list1[x][1]==seclo:
            result.append(list1[x][0])
    for i in result:
        print(i)