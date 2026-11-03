def structure(a):
    for i in range(1,a+1):
        for j in range(1,a+1):
            if i==1 or i+j==a+1:
                print("*",end="")
            else:
                print(" ",end="")
        print()
structure(7)

