# Frequency of function

def frequency():
    s=input("enter the sentence:")
    f={}
    for i in s:
        if i.isalpha():
            #i=i.lower()
            if i in f:
                f[i]+=1
            else:
                f[i]=1
                
    print("letter frequency:")
    for i in f:
        print(i,":",f[i])
        
n=frequency()

    