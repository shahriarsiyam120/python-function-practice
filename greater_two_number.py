def great(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
   
n=int(input("enter first number :"))    
m=int(input("enter second number:"))
greater=great(m,n)
print("the greater number is :",greater)