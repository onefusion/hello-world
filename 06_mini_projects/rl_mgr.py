def show_menu():
    print("\nRocket League Player Manager")
    print("1. Add player")
    print("2. Remove player")
    print("3. List players")
    print("4. List players sorted by MMR")
    print("5. Quit")

def list_players(players):
    if not players:
        print("\nNo players have been added yet.")
        return

    print("\nCurrent players:")
    for gamertag, mmr in players.items():
        print(f"    {gamertag}: {mmr} MMR")

def list_players_sorted(players):
    if not players:
        print("\nNo players have been added yet.")
        return

    print("\nPlayers sorted by MMR (highest first):")
    sorted_players = sorted(players.items(), key=lambda item: item[1], reverse=True)

    for rank, (gamertag, mmr) in enumerate(sorted_players, start=1):
        print(f"    {rank}, {gamertag}: {mmr} MMR")

def get_mmr_from_user():
    while True:
        mmr_input = input("Enter MMR (numeric value like 1500): ")
        try:
            mmr = int(mmr_input)
            if mmr < 0:
                print("MMR cannot be negative. Try again.")
                continue
            return mmr
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_player(players):
    gamertag = input("Enter player gamertag: ").strip()

    if not gamertag:
        print("Gamertag cannot be empty.")
        return

    if gamertag in players:
        print(f"{gamertag} already exists with {players[gamertag]} MMR.")
        choice = input("Do you want to update their MMR? (y/n): ").lower()
        if choice != "y":
            return

    mmr = get_mmr_from_user()
    players[gamertag] = mmr
    print(f"Player '{gamertag}' set to {mmr} MMR.")

def remove_player(players):
    if not players:
        print("\nNo players to remove.")
        return
        
    gamertag = input("Enter the gamertag to remove: ").strip()

    if gamertag in players:
        remove_mmr = players.pop(gamertag)
        print(f"Remove player '{gamertag}' (MMR: {remove_mmr}).")
    else:
        print(f"No player found with gamertag '{gamertag}'.")

def main():
    players = {}

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_player(players)
        elif choice == "2":
            remove_player(players)
        elif choice == "3":
            list_players(players)
        elif choice == "4":
            list_players_sorted(players)
        elif choice == "5":
            print("Exiting. GGs!")
            break
        else:
            print("Invalid choice. Please pick a number from 1 to 5.")

if __name__ == "__main__":
    main()