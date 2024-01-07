player1=0
player2=0
total=0
value=[1,2,3,4,5,6,7,8,9,10]
print("only enter 1-10 value only: ")
while(total<100):
    player1=int(input("player 1:"))
    if player1 in value:
        total+=player1
        print(total)
    else:
        print("warnning! remmamber the rule !")
        player2 = int(input("player 2:"))
        total += player2
        player2 = total
        print(total)
    player2 = int(input("player 2:"))
    if player2 in value:
        total += player2
        print(total)
        print("------------------------------------")
    else:
        print("warnning! remmamber the rule !")
        player2 = int(input("player 2:"))
        total += player2
        player2=total
        print(total)
        print("------------------------------------")
        
if player1==100:
    print("the winner is player 1")
else:
    print("the winner is player 2:")
