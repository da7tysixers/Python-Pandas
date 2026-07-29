import random

computer_choice = random.choice(["rock", "paper", "scissors"])
user_choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()


for i in range(3):
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()
    else:
        break
for i in range(3):
    if computer_choice == user_choice:
        print(f"Both chose {computer_choice}. It's a tie!")
        play_again = input("Do you want to play again? (yes/no): ").lower().strip()
        if play_again == "yes":
            computer_choice = random.choice(["rock", "paper", "scissors"])
            user_choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()
        else:
            print("Thanks for playing!")
            break

    elif (computer_choice == "rock" and user_choice == "scissors"):
        print(f"Computer chose {computer_choice}. You lose!")
        play_again = input("Do you want to play again? (yes/no): ").lower().strip()
        if play_again == "yes":
            computer_choice = random.choice(["rock", "paper", "scissors"])
            user_choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()
        else:
            print("Thanks for playing!")
            break
    elif (computer_choice == "paper" and user_choice == "rock"):
        print(f"Computer chose {computer_choice}. You lose!")
        play_again = input("Do you want to play again? (yes/no): ").lower().strip()
        if play_again == "yes":
            computer_choice = random.choice(["rock", "paper", "scissors"])
            user_choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()
        else:
            print("Thanks for playing!")
            break  
    elif (computer_choice == "scissors" and user_choice == "paper"):
        print(f"Computer chose {computer_choice}. You lose!")
        play_again = input("Do you want to play again? (yes/no): ").lower().strip()
        if play_again == "yes":
            computer_choice = random.choice(["rock", "paper", "scissors"])
            user_choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()
        else:
            print("Thanks for playing!")
            break
    elif (user_choice == "rock" and computer_choice == "scissors"):
        print(f"You chose {user_choice}. You win!")
        play_again = input("Do you want to play again? (yes/no): ").lower().strip()
        if play_again == "yes":
            computer_choice = random.choice(["rock", "paper", "scissors"])
            user_choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()
        else:
            print("Thanks for playing!")
            break
        
    elif (user_choice == "paper" and computer_choice == "rock"):
        print(f"You chose {user_choice}. You win!")
        play_again = input("Do you want to play again? (yes/no): ").lower().strip()
        if play_again == "yes":
            computer_choice = random.choice(["rock", "paper", "scissors"])
            user_choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()
        else:
            print("Thanks for playing!")
            break
    elif (user_choice == "scissors" and computer_choice == "paper"):
        print(f"You chose {user_choice}. You win!")
        play_again = input("Do you want to play again? (yes/no): ").lower().strip()
        if play_again == "yes":
            computer_choice = random.choice(["rock", "paper", "scissors"])
            user_choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()
        else:
            print("Thanks for playing!")
            break
    else:
        print("Invalid choice. Please choose rock, paper, or scissors.")