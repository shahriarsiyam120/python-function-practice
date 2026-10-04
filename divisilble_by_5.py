def check(num):
    if num%5==0:
        return "divislble"
    else:
        return "not divislble:"
    
n=int(input("enter a number:"))
div=check(n)
print(div)   
     