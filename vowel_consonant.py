def cheack_letter(letter):
    if letter in "aeiouAEIOU":
        return "vowel"
    else:
        return "consonant"
    
n=input("enter a letter:")
print(cheack_letter(n))    