'''rock paper scissors'''


'''
rock beats scissors
scissors beats paper
paper beats rock
'''


import random

def rock_paper_scissors():
    dict_choice = {
    "rock": -1,
    "paper": 0,
    "scissors": 1
}
    while True:
        computer_choice = cc = random.randint(-1, 1)
        for index, (key, value) in enumerate(dict_choice.items(), start=1):
            print(f"{index}. {key}: {value}")
        try:
            player_choice = pc = int(input("enter your choice (-1, 0, 1): ").strip())
            if cc == -1 and pc == -1:
                print(f"Tie, computer chose 'rock' and you chose 'rock'.")
            elif cc == 0 and pc == 0:
                print(f"Tie, computer chose 'paper' and you chose 'paper' .")
            elif cc == 1 and pc == 1:
                print(f"Tie, computer chose 'scissors' and you chose 'scissors' .")
            elif cc == -1 and pc == 0:
                print(f"You win, computer chose 'rock' and you chose 'paper' .")
            elif cc == -1 and pc == 1:
                print(f"Computer win, computer chose 'rock' and you chose 'scissors' .")
            elif cc == 0 and pc == -1:
                print(f"Computer win, computer chose 'paper' and you chose 'rock' .")
            elif cc == 0 and pc == 1:
                print(f"You win, computer chose 'paper' and you chose 'scissors' .")
            elif cc == 1 and pc == 0:
                print(f"Computer win, computer chose 'scissors' and you chose 'paper' .")
            elif cc == 1 and pc == -1:
                print(f"You win, computer chose 'scissors' and you chose 'rock' .")
            else:
                print("Invalid choice! plz enter number out of -1, 0, 1.")
        except ValueError:
            print("Invalid input! plz enter a valid input.")
                
rock_paper_scissors()