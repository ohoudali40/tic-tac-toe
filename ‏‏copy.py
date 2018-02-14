g = [0,0,0,0,0,0,0,0,0]
a = [1,2,3,4,5,6,7,8,9]
print(g[0],"|",g[1],"|",g[2])
print("______")
print(g[3],"|",g[4],"|",g[5])
print("______")
print(g[6],"|",g[7],"|",g[8])
y = 1
z = 9
x = "true"
while x == "true":
    print("Player ",y)

    if y == 1:
        n = int(input("Enter Even Number: "))

    elif y == 2:
        n = int(input("Enter Odd Number: "))

    b = int(input("Enter the place: "))
    z = z - 1

    for i in range(0,z):
        if a[i] == b:
            a.remove(b)
            g.pop(b-1)
            g.insert(b-1,n)

            for j in range(0,z):

                for f in range(0,z):

                    if (a[i]!=1 and a[j]!=2 and a[f]!=3):
                        if(g[0]+g[1]+g[2]==15):
                            x = "false"

                    elif(a[i]!=4 and a[j]!=5 and a[f]!=6):
                        if(g[3]+g[4]+g[5]==15):
                            x = "false"

                    elif (a[i]!=7 and a[j]!=8 and a[f]!=9):
                        if(g[6]+g[7]+g[8]==15):
                            x = "false"

                    elif(a[i]!=1 and a[j]!=4 and a[f]!=7):
                        if(g[0]+g[3]+g[6]==15):
                            x = "false"

                    elif(a[i]!=2 and a[j]!=5 and a[f]!=8):
                        if(g[1]+g[4]+g[7]==15):
                            x = "false"

                    elif(a[i]!=3 and a[j]!=6 and a[f]!=9):
                        if(g[2]+g[5]+g[8]==15):
                            x = "false"

                    elif(a[i]!=1 and a[j]!=5 and a[f]!=9):
                        if(g[0]+g[4]+g[8]==15):
                            x = "false"

                    elif(a[i]!=3 and a[j]!=5 and a[f]!=7):
                        if(g[2]+g[4]+g[6]==15):
                            x = "false"
                    if x == "false":
                        break
                if x == "false":
                    break
            if x == "false":
                break
    o = y
    if y == 2:
        y = 1
    else:
        y += 1
    print("End")
    print(g[0],"|",g[1],"|",g[2])
    print("______")
    print(g[3],"|",g[4],"|",g[5])
    print("______")
    print(g[6],"|",g[7],"|",g[8])

print("THE WINNER IS PLAYER ",o)
                
