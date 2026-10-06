import random

while True:
    print("="*32)
    print(" "*5+"KKingFish Log System" + " "*5)
    print("="*32)
    print("1. Log a New Catch")
    print("2. Exit")
    print("="*32)
    menuInput = input(">> ")
    if menuInput == "1":
        while True:
            anglerName = input("Input Angler name: ")
            if len(anglerName) <= 3:
                print("Angler name must be more than 3 characters!")
                continue
            elif not anglerName.replace(" ","").isalpha():
                print("Angler name can only contain letters and spaces!")
                continue
            break

        while True:
            fishSpecies = input("Input fish species (Tuna/Salmon/Bass/Marlin): ")
            if fishSpecies not in ("Tuna", "Salmon", "Bass", "Marlin"):
                print("Fish species must be Tuna/Salmon/Bass/Marlin!")
                continue
            break

        while True:
            try:
                fishWeight = int(input("Input fish weight (kg): "))
            except ValueError:
                print("Fish weight must be numeric!")
                continue

            if fishWeight < 0:
                print("Fish weight must be a positive number!")
                continue
            break

        while True:
            catchLoc = input("Input Catch Location (River/Lake/Sea/Pond): ")
            if catchLoc not in ("River", "Lake", "Sea", "Pond"):
                print("Catch location must be in River/Lake/Sea/Pond!")
                continue
            break

        while True:
            RodType = input("Input Rod Type (Spinning/Casting): ")
            if RodType not in ("Spinning", "Casting"):
                print("Rod type must be either Spinning or Casting!")
                continue
            break

        LogID = "KK"
        for i in range(1,5):
            LogID += str(random.randint(0,9))

        FishSize_Category = ""
        if fishWeight < 5:
            FishSize_Category = "Small Fry"
        elif fishWeight >= 5 and fishWeight <= 15:
            FishSize_Category = "Decent Catch"
        elif fishWeight > 15:
            FishSize_Category = "Trophy Fish"

        Pounds = fishWeight * 2.20462

        print("="*32)
        print(" "*5 + "Fish Catch Logged!" + " "*5)
        print("="*32)
        print(f"Log ID: {LogID}")
        print(f"Angler Name: {anglerName}")
        print(f"Fish Species: {fishSpecies}")
        print(f"Catch Location: {catchLoc}")
        print(f"Rod Type: {RodType}")
        print("-"*32)
        print(f"Weight (kg): {fishWeight}")
        print(f"Weight (lbs): {Pounds:.2f}")
        print(f"Size Category: {FishSize_Category}")
        print("="*32)

        input("Press Enter to return to the main menu...")
        continue
    elif menuInput == "2":
        print("Thank you for using KKingfish Log System! Goodbye!")
        break
    else:
        print("Please input between 1 or 2!")
        continue
    
