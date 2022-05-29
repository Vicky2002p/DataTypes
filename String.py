#Vivek

mystr = input("Enter a string with characters not less than 6 ")
if len(mystr)<6:
    print(f"{mystr} is not a valid str")
elif mystr.isalpha():
    print("You have entered a valid alphabetic string.")
else:
    print(f"{mystr} is a valid non-alphabetic str.")
    print(f"The index of the first 'e' in {mystr} is {mystr.index('e')}")
print(f"The number of character in {mystr} is {len(mystr)}")