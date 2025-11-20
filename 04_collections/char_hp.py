def show_chars(chars):
    print("\nCurrent characters:")
    if not chars:
        print("  (None yet)")
    else:
        for name, hp in chars.items():
            print(f"  {name}: {hp} HP")


def damage_char(chars, name, amount):
    if name not in chars:
        print(f"{name} does not exist.")
        return

    chars[name] -= amount
    if chars[name] < 0:
        chars[name] = 0 # Min hp
    print(f"{name} takes {amount} damage! Now at {chars[name]} HP.")


def heal_char(chars, name, amount):
    if name not in chars:
        print(f"{name} does not exist.")
        return
        
    chars[name] += amount
    print(f"{name} heals {amount} HP! Now at {chars[name]} HP.")


def main():
    chars = {}

    while True:
        print("\nMenu:")
        print("1. Add character")
        print("2. Damage character")
        print("3. Heal character")
        print("4. Show all characters")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter character name: ")
            hp = int(input("Enter starting HP: "))
            chars[name] = hp
            print(f"Added {name} with {hp} HP.")

        elif choice == "2":
            name = input("Character to damage: ")
            amount = int(input("Amount of damage: "))
            damage_char(chars, name, amount)

        elif choice == "3":
            name = input("Character to heal: ")
            amount = int(input("Amount to heal: "))
            heal_char(chars, name, amount)

        elif choice == "4":
            show_chars(chars)

        elif choice == "5":
            print("Exiting.")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
