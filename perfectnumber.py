num=int(input("Enter the number: "))  
ans=0  
for i in range(1,num):  
    if (num%i==0):  
        ans=ans+i  
if(ans==num):  
    print("The entered number is a perfect number")  
else:  
    print("The entered number is not a perfect number")  
