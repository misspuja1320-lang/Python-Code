# count character in file

f=open("file1.txt","r")
d=f.read()
f.close()
c={}
for i in d:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
for i in c:
    if(c[i]=1):
        print(i,":",c[i])