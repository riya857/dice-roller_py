import random 
while True:
    input("press enter to roll the dice...")
    print("you rolled:",random.randint(1,6))
    again=input("roll again?(y/n):")
    if again.lower()!='y':
        break