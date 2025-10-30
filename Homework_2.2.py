# Homework 2.2.: FizzBuzz

number =int(input("Vnesi številko med 1 in 100"))

for i in range (1,1+number):
    if i % 3 ==0:
        print("Fizz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 ==0 and i % 5 ==0:
        print("FizzBuzz")
    else:
        print(i)