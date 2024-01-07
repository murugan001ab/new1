if __name__ == '__main__':
    list1=[]
    score=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])
        score.append(score)
    score=list(set(score))
    score.remove(min(score))
    i=score.index(min(score))
    print(name[i])
    
