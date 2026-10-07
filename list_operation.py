n=int(input("Enter the number:\t"))
L=[]
for i in range(1,n+1):
    L.append(i)
print("L=",L)
while(1):
    print("1. Add")
    print("2. Edit")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if(choice=='1'):
        item=int(input("Enter item:"))
        L.append(item)
        print(L)
        
    elif(choice=='2'):
        index=int(input("Enter index number:"))
        if(index<len(L)):
            item=int(input("Enter item:"))
            L[index]=item
            print("item update")
        else:
            print("invalid item")
        
    elif(choice=='3'):
        item=int(input("Enter item:"))
        L.remove(item)
        print("item deleted",item)

        
    elif(choice=='4'):
        print("display list:",L)
        
    elif(choice=='5'):
        print("exit")
        break
        
    else:
        print("invalid")
        break