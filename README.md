#Exercise 2.1.

ime = input("Kako ti je ime?")
print(f"Živijo {ime}")
print("Ta program pretvarja kilometre v milje")

while True:
    kilometri=float(input("Vnesi razdaljo v kilometrih:"))

    milje = kilometri * 0.621
    print(f"{kilometri} kilometrov je enako {milje} milj.")

    ponovno = input("Ali si želiš pretvoriti novo številko?")
    if ponovno != "da" :
       print("Hvala, nasvidenje!")
       break

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
# Homework 2.3. Make string lowercase
x = input("Would you like to continue(yes/no)?")
x = x.lower()

if x == "yes":
    print("Great, lets cotinue")
elif x == "no":
    print("Okay, have a nice day!")

