if __name__ == '__main__':
    list1=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])
    print(list1)
    
    print(list1.index(max(score)))
    
  #  print(name[max(score)])
