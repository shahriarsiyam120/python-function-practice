def cel_to_far(cel):
    far=(cel*9/5)+32
    return far 
temperature=int(input("enter the temperature in celsius:"))
result=cel_to_far(temperature)
print("the temperature in fahrenheit is:",result)