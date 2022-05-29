#Vivek

list1 = ['bananaa', 'grapes', 'pears','peaches','apples','plums','oranges']
print(list1)
sum = 0
for item in list1:
    print(item)
    if item[0] == 'a':
        print("The word has its first letter as a",item)
        break
    else:
        sum += len(item)
print(sum)

