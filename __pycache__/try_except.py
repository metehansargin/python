def divide(number1,number2):
    try:
        number1_int=int(number1)
        number2_int=int(number2)
        return number1_int/number2_int
    except ValueError:
        return "only integers are allowed !  Try again"
    except ZeroDivisionError:
        return "you cannot divide any number by zero"
number1=input("please provide a number1 :")
number2=input("please provide a number2 :")
print(divide(number1,number2))