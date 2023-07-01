for i in range(1,10):
    for j in range(1,10):
        if j==1 or j==9 and i==1 or i==9:
            print(5, end=" ")
        if j==2 or j==8 or (i==2 and(j!=1 and j!=9)):
            print(4, end=" ")
        if j==3 or j==7 or (i==3 and(j!=[1,2] and j!=[8,9])):
            print(3, end=" ")
        if j==4 or j==6 or (i==4 and(j!=[1,2,3] and j!=[7,8,9])):
            print(2, end=" ")
        if j==5 or j==5 or (i==5 and(j!=[1,2,3,4] and j!=[6,7,8,9])):
            print(1, end=" ")
    print('\n')


        