phone_book={"Hami Kaya":"0987667785","Selin Sert":"098654132","Fatih Falcı":"0986541324"}
print(phone_book["Hami Kaya"])

inventory=dict()
inventory["bananas"]=19
inventory["watermelon"]=25
inventory["apple"]=10
inventory["grape"]=99
inventory["strawberry"]=300

print(inventory)
print(inventory.keys())
print(inventory.values())
print(inventory.items())

for key,value in inventory.items():
    if value>200:
        print("too many",key)
    else:
        print("enough",key)