def cheack_age(age):
    if age>=18:
        return "adult"
    else:
        return "minor"
    
n=int(input("enter your age:"))
print(cheack_age(n))    