#python program to create a simple calculator
def add(x,y):
    return x+y
def sub (x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def avg(x,y):
    return (x+y)/2
print("select operation")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
print("5.avg")

select=int(input("enter your choice(1/2/3/4/5):"))  

x=int(input("enter first number:"))
y=int(input("enter second number:"))

if select==1:
    print("the sum of two number is:",add(x,y))
elif select==2:
    print("the sub of two number is:",sub(x,y))
elif select==3:
    print("the mul of two number is:",mul(x,y))
elif select==4:
    print("the div of two number is:",div(x,y))
elif select==5:
    print("the avg of two number is:",avg(x,y))
else:
    print("invalid input")