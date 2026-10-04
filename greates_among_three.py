def check(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3

n=int(input("enter first number:"))
m=int(input("enter second number:"))
p=int(input("enter third number:"))
greates=check(n,m,p)
print("gretaes:",greates)