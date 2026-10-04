def cheack(num):
    if num%5==0 and num%10==0:
        return "Divisible"
    else:
        return "not Divisible"
    
n=int(input("enter a number :"))    
print(cheack(n))