def hanoi(n,s,d,a):
    if(n==1):
        print("move disk",1,"from source to",s,"destination",d)
        return
    hanoi(n-1,s,a,d)
    print("move disk",n,"from source to",s,"destination",d)
    hanoi(n-1,a,d,s)
n=int(input("enter number of disk"))
hanoi(n,'A','B','C')




