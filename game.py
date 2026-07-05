import random
choice = ["stone","paper","scissor"]
comp = random.choice(choice)

print("==========Stone-Paper-Scissor==========")
user = input("Enter name: ").title()
print(f"Welcome {user} to game.")
while True:
    user = input("Enter your choice[stone,paper,scissor]: ").lower().strip()
    if user == comp:
        print("Draw!")
        print(f"computer choose {comp} and you choose {user}.")
    elif user == "stone" and comp == "scissor" or user == "scissor" and comp == "paper":
        print("You Win!")
        print(f"computer choose {comp} and you choose {user}.")
        break
    elif user not in choice:
        print("Invalid!")
    else:
        print("You loss!")
        print(f"computer choose {comp} and you choose {user}.")
