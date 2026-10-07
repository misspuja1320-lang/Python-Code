# string operation

s=input("Enter a string:")
print("\n 1. frequency of character.\n 2. replace character.\n 3. remove first occurence.\n 4. remove all occurence.\n 5. exit\n")
while 1:
    ch=input("enter the choice:")
    if ch=='1':
        char=input("enter the character:")
        f=s.count(char)
        print("frequency of character:",f)
    elif ch=='2':
        old=input("enter old character:")
        new=input("enter new character:")
        r=s.replace(old,new)
        print("replace character:",r)
    elif ch=='3':
        char=input("enter the first remove occurence:")
        r=s.replace(char," ",1)
        print("result:",r)
    elif ch=='4':
        char=input("enter remove occurence:")
        r=s.replace(char," ")
        print("result:",r)
    elif ch=='5':
        print("exiting")
        break
    else:
        print("invalid")
        break