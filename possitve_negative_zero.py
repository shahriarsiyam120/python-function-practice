def check_number(num):
    if num>0:
        return "possitve"
    elif num<0:
        return "negative"
    else:
        return "zero"
    
num=int(input("enter a number:"))
result= check_number(num)
print(result)    