import random

while True:
    try:
        Choice = int(input("Choose (1:'✌️ Scissors',"  ",2:'✊ Rock',"  "3:'✋ Paper'): "))
        if Choice not in [1, 2, 3]:
            print("❌ Please enter a number between 1 and 3")
            continue
        
        computer = random.choice([1, 2, 3]) 
        
        if (Choice == 1 and computer == 3) or (Choice == 2 and computer == 1) or (Choice == 3 and computer == 2):
            print("🎉 You Win!")
            break 
        elif Choice == computer:
            print("😐 Draw! Try again.")
        else:
            print("😢 You lose")
            
    except ValueError:
        print("❌ Please enter a valid number.")
