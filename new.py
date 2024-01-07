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
    for i in range(len(list1)):
        if list1[i][1]==seclo:
            result.append(name)
    print(result)
