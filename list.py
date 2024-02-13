shopping_list=["apple","juice","ball","bread"]

shopping_list.append("water")
print(shopping_list)
shopping_list.insert(2,"egg")
print(shopping_list)
shopping_list.remove("water")
print(shopping_list)
shopping_list[3]="strawberry"
print(shopping_list)

language_list=("turkish","french","english","germany")
item1,item2,item3,item4=language_list
print(item1)
print(item2)
print(item3)
print(item4)
print(language_list[0])


number_list=[1,2,3,4,5]
square_list=[]
for num in number_list:
    square_list.append(num**2)
print(square_list)

