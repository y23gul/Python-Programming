letter = input("Enter a letter: ")
if letter in "aeiou":
    print("Vowel")
elif letter == "y":
    print("It depends")
elif letter in "1234567890":
    print("Number")
elif letter in "bcdfghjklmnpqrstvwxz":
    print ("Consonant")
else:
    print("N/A")
