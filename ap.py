def simulate_battle():
    """
    Simulates the battle between player's army and enemy's army.
    """
    enemy_army_size = random.randint(180000, 220000)
    your_army_size = random.randint(40000, 80000)

    print("The battle begins!")
    print(f"You are facing an enemy army of {enemy_army_size} soldiers.")
    print(f"Your army consists of {your_army_size} soldiers.")

    round_count = 0
    cavalry_charge_round = 10
    momentum = False

    while enemy_army_size > 0 and your_army_size > 0:
        round_count += 1
        time.sleep(1)
        your_loss = random.randint(1000, 5000)
        enemy_loss = random.randint(1000, 5000)

        print("---------------------------------------------------------------")
        print("Both sides clash!")

        if round_count == cavalry_charge_round:
            charge_choice = input("Round 10: Do you want to conduct a cavalry charge (C) or retreat (R)? ").upper()
            if charge_choice == "C":
                charge_success = random.random() < 0.49
                if charge_success:
                    print("You ordered a cavalry charge!")
                    print("The charge was successful!")
                    enemy_loss += 1500
                else:
                    print("You ordered a cavalry charge!")
                    print("The charge failed, and the enemy gains momentum!")
                    momentum = True
            elif charge_choice == "R":
                print("You chose to retreat.")
                break

        if momentum:
            your_loss *= 2

        your_army_size -= your_loss
        enemy_army_size -= enemy_loss

        print(f"You lost {your_loss} soldiers. Your army size: {your_army_size}")
        print(f"The enemy lost {enemy_loss} soldiers. Enemy army size: {enemy_army_size}")

        if your_army_size <= 0:
            print("Unfortunately, your army has been defeated. You lose!")
            break

        if enemy_army_size <= 0:
            print("Congratulations! You have won the Battle of Poltava!")
            break

        # Check for the retreat condition
        if round_count > 5 and your_army_size >= 1.6 * enemy_army_size:
            retreat_chance = random.random()
            if retreat_chance <= 0.75:
                print("The enemy decides to retreat!")
                enemy_army_size = int(enemy_army_size * 0.25)  # Enemy retreats with 75% of their army

    print("---------------------------------------------------------------")
