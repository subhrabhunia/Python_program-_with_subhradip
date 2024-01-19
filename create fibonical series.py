val=int(input("enter the limit"))
temp1=0
temp2=1
backup=0
print("the series is:")
for i in range (1,val):
    print(temp1)
    backup=temp2
    temp2=temp1+temp2
    temp1=backup
