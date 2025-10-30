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

