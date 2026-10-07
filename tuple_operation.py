t1=(1,2,5,7,9,2,4,6,8,10)
while(1):
    print("\n 1. t1 in 2 separate line \n")
    print("2. all even value of t1 as another tuple t2 \n")
    print("3. concatenate of two tuple \n")
    print("4. return maximum and minimum value from t1\n ")
    print("5. Exit \n")
    
    ch=int(input("Enter your choice:"))
    
    if(ch==1):
        print("length:",len(t1))
        sep=len(t1)//2
        print("Separate of 2 lines:")
        print(t1[:sep])
        print(t1[sep:])
    elif(ch==2):
        print("all even number:")
        for i in t1:     
            if(i%2==0):          
                print(i,end=' ')
    elif(ch==3):
        t2=(11,13,15)
        print("t2=",t2)
        t3=t1+t2
        print("concatenate=",t3)
    elif(ch==4):
        print("maximum value of t1:",max(t1))
        print("minimum value of t1:",min(t1))
    elif(ch==5):
        print("exiting")
        break
    else:
        print("invalid")
        break