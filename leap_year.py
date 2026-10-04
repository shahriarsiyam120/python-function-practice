def cheack_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return "leap year"
    else:
        return "not year"
    
    
    
n=int(input("enter a year:"))
print(cheack_year(n))