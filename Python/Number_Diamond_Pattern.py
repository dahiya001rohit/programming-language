n = int(input())
for i in range(1,n+1):
    for j in range (n-i):
        print(" ",end=" ")
    for k in range (i):
        print(k +1 ,end=" ")
    for l in range (i-1,0,-1):
        print(l,end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range (n-i):
        print(" ",end=" ")
    for k in range (i):
        print(k +1 ,end=" ")
    for l in range (i-1,0,-1):
        print(l,end=" ")
    print()
