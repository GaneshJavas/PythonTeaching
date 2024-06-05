def disGame(t):
    print(" {} | {} | {}".format(t[0],t[1],t[2]))
    print("---|---|---")
    print(" {} | {} | {}".format(t[3],t[4],t[5]))
    print("---|---|---")
    print(" {} | {} | {}".format(t[6],t[7],t[8]))

t = [0,1,2,3,4,5,6,7,8]
disGame(t)
for i in range(9):
    a = int(input("Player {} your turn: ".format(i%2+1)))
    if type(t[a]) == int and i%2 == 0 :
        t[a] = "X"
    elif type(t[a]) == int and i%2 != 0:
        t[a] = "O"
    disGame(t)
    
    if (t[0] == t[1] == t[2]) or (t[3] == t[4] == t[5]) or (t[6] == t[7] == t[8]) or (t[0] == t[3] == t[6]) or (t[1] == t[4] == t[7]) or (t[2] == t[5] == t[8]) or (t[0] == t[4] == t[8]) or (t[2] == t[4] == t[6]):
        print("Player {} WIN".format(i%2+1))
        break
    else:
        if i == 8:
            print("DRAW")
        else:
            continue 