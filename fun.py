import random
comp = random.randint(1,100)
name = input("enter name: ").capitalize()
print(f"Welocome {name}.")
attempts = 0
while True:
    print("="*40)
    print("\tNumber Gurssing Game!\t")
    print("="*40)
    user = int(input("Guess between(1 to 100): "))
    if user == comp:
        print("you won!")
        print(f"computer choose {comp} and you guess in {attempts} turns.")
        break
    elif user > comp:
        print("THe number is lower.")
    elif user < comp:
        print("THe number is higher.")
    else:
        print("Invalid!")
    attempts += 1
    