try:
    number1 = int(input("enter a number:"))
    number2 =int(input("enter another number :"))
    result = number1 / number2

except ZeroDivisionError:
    print("you can not divide by zero!")

exept ValueError :
 print("please enter a valid number")

else:
      print("division successfull result is : ",result)

finally:
    print("this block always runs")
    my_list = [1,2,3]
    print(my_list[1])
