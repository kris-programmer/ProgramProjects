import random

while True:
    choice = (input("Roll the dice? (y/n) ")).lower()
    if choice == 'y':
        print("Rolling...")
        random_num_1 = random.randint(1, 6)
        random_num_2 = random.randint(1, 6)
        print(f"Rolled ({random_num_1}, {random_num_2})")
        break
    elif choice == 'n':
        print("Exiting...")
        break
    else: 
        print("Invalid choice!")