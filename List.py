#Vivek

#Taking input
fav_animal = input("Enter your favorite animal in lowercase letters: ")
#Converting the input to uppercase
fav_animal = fav_animal.upper()
print(f"Oh, so {fav_animal} is ur favorite animal")
#Replacing the a character in the string and printing
new_str = fav_animal.replace("O", "*")              
print(f"How about we dont use the letter 'o' in this word! Then we have {new_str}")
#Taking input and printing
fav_num = int(input("Enter your 2 digit favorite number between 10 to 99: "))
print(f"So, is {fav_num} your lucky number as well?")
#Making a list and printing
list1 = ['red','blue','yellow','green','red','pink',1,[2,3]]
print(list1)
#Manupulating the list
print(list1[2][-3:])
print(list1[3:])
#Adding the input on an index
list1.insert(0, input("Enter a new colour: "))
print(f"The updated list looks like: {list1}")
res = len(list1) - fav_num
print(f"The number elements in the list is {len(list1)}")
print(f"res {res}")

