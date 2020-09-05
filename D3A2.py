#Assignment-2 Day3
#Prime Numbers between 1 to 200
l=1
u=200

for i in range(l,u+1):
    flag=0
    if i>1:
        for j in range(2,i//2+1):
            if i%j==0:
                flag=1
                break
        if flag==0:
            print(i,end=" ")
        