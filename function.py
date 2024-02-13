def hello(name):
   print("merhaba",name)

hello("metehan")
 
def sum(number,number2):
   answer=number+number2
   return answer    #eger buraya return eklemezsek none deger donecek. Onun için return kullanmamız lazım

geri=sum(10,9)
print(geri)

"""def control(firstName,lastName,bool=True):
   if auto_correction==True:
      capasitilized_firstname=firstName.capatilize()
      capasitilized_lastname=lastName.capatilize()
      print("hello",capasitilized_firstname,capasitilized_lastname)
   else:
      print("hello",firstName,lastName)

control("metehan","SaRgın",True)"""
def car(brand,model,colour):
   print("My favourite car is",brand,"in the model",model,colour)

car("R8","audi","green")
car(colour="black",brand="R8",model="audi")
#car(colour="audi",model="black","R8") hatalı yazım
 
number=13
def change_number():
 number=4   

change_number()
print(number)

