hello_file=open("hello.txt","w")
hello_file.write("Merhaba Dünya,Pyhton")
hello_file.close()

import random
numbers_file=open("number_history.txt","w")
while True:
    random_number=random.randrange(1000)
    print(random_number)
    numbers_file.write(str(random_number))
    numbers_file.write("\n")
    if random_number==777:
        print("Found !")
        break
numbers_file.close()
