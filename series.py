# 1-2+3-4+5.............-n

n=int(input("Enter the number:"))
s=0
for i in range(1,n+1):
    print(i,end='')
    if(i%2==0):
	    s=s-i
    else:
	    s=s+i
print("\nSum of series:\t",s)