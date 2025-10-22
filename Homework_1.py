# 1.1. The mood checker
mood = input ("Kako si danes?")
if mood == "happy":
    print("It is great to see you happy!")
elif mood== "nervous":
    print("Take a deep brath 3 times.")
elif mood == "sad":
    print("How can i help you?")
elif mood == "excited":
    print("Mee tooo girl!")
elif mood == "relaxed":
    print ("Happy for you")
else:
    print("I don't know how to help you.")

#1.2. Guess the secret number
secret = 10

guess = int(input("Guess the number between 0 and 20"))

if guess == secret:
    print("Cograts")
else:
    print("Wrong number try again.")

#1.3. Simple calculator

st_ena = float(input("Vpiši prvo število"))

st_dve = float(input("Vpiši drugo število"))

operacija = input("Vpiši operacijo +,- ,*. /")

if operacija == "+":
   rezultat =st_ena +st_dve
   print("Rezultat", rezultat)
elif operacija == "-":
    rezultat =st_ena -st_dve
    print("Rezultat", rezultat)
elif operacija == "*":
    rezultat=st_ena * st_dve
    print("Rezultat", rezultat)
elif operacija == "/":
    rezultat=st_ena/ st_dve
    print("Rezultat", rezultat)
else:
    print("Napaka")







