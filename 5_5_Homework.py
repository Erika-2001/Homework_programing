import random
import json
import datetime




def get_score_list():
    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())
    return score_list

def top_scores():
    score_list = get_score_list()
    for score_dict in score_list:
        print ("Name: " + score_dict ["name"] + "with" + str(score_dict["attempt"]) + "attempt, date"+ score_dict["date"])

def play_game():
    secret = random.randint(1,30)
    attempt = 0
    name = input("Hello, what is your name:")
    wrong_guesses = []    
    
    score_list = get_score_list()

    while True:
        guess = int(input("Guess the secret number (between 1 and 30):"))
        attempt += 1

        if guess == secret:
             print("You've guessed it! Your secret number is", str(secret))
             print(f"Attempts needed:{attempt}")     
             
             score_list.append({"attempt": attempt, "date": str(datetime.datetime.now()),"name": name, "secret_number":secret, "wrong_guesses": wrong_guesses})
             
             with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list)) 
                break
        
        elif guess > secret:
            print("Your guess is too high, try something smaller.")
            wrong_guesses.append(guess)
       
        else:
            print("Your guess is too samll, try something higher.")
            wrong_guesses.append(guess)

play_game()
