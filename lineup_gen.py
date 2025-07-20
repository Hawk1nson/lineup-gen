import random
import csv

# Dictionary mapping initials to full names
players_dict = {
    'AG': 'Anders Greenwell',
    'EG': 'Eli Gergen',
    'LH': 'Lincoln Hawkinson',
    'CF': 'Carter Funk',
    'IP': 'Ian Peterson',
    'LC': 'Landon Carey',
    'CB': 'Christian Black',
    'LA': 'Luke Atkinson',
    'ZT': 'Zach Tolscer',
    'JS': 'Jaxon Smith'
}

# Forbidden pairs using initials
forbidden_pairs = [
    ('LA', 'CF'), ('EG', 'CF'), ('LC', 'CF'),
    ('LA', 'JS'), ('EG', 'JS'), ('LC', 'JS')
]

all_players = list(players_dict.keys())

# Ask how many players are out
while True:
    user_input = input("How many players are not playing? (0–10 or 'x' to quit): ").strip().lower()

    if user_input == "x":
        print("👋 Exiting program.")
        exit()

    if not user_input.isdigit():
        print("❌ Please enter a number or type 'x' to quit.")
        continue

    num_out = int(user_input)
    if num_out < 0 or num_out > len(all_players):
        print(f"❌ Please enter a number between 0 and {len(all_players)}.")
        continue

    if num_out == len(all_players):
        print("❌ All players are out — no lineup can be generated.")
        continue

    # Ask for initials of players not playing
    not_playing = []
    for i in range(num_out):
        while True:
            initials = input(f"Enter initials for player {i + 1} not playing (or 'x' to quit): ").strip().upper()
            if initials.lower() == "x":
                print("👋 Exiting program.")
                exit()
            elif initials not in all_players:
                print("❌ Initials not found in player list.")
            elif initials in not_playing:
                print("⚠️ You already entered that player.")
            else:
                not_playing.append(initials)
                break

    active_players = [p for p in all_players if p not in not_playing]
    break  # Done collecting input

# Validity check
def is_valid_lineup(lineup):
    for i in range(len(lineup) - 1):
        if (lineup[i], lineup[i + 1]) in forbidden_pairs:
            return False
    return True

# Lineup generator
def generate_valid_lineup(players, forbidden_pairs, max_attempts=10000):
    attempts = 0
    while attempts < max_attempts:
        shuffled = players[:]
        random.shuffle(shuffled)
        if is_valid_lineup(shuffled):
            return shuffled
        attempts += 1
    return None

# Loop: keep generating until user accepts or exits
while True:
    lineup = generate_valid_lineup(active_players, forbidden_pairs)
    if not lineup:
        print("❌ Could not generate a valid lineup after many attempts.")
        exit()

    print("\n✅ Valid Batting Lineup:")
    for i, initials in enumerate(lineup, start=1):
        print(f"{i}. {players_dict[initials]} ({initials})")

    choice = input("\nAccept this lineup? (y = yes / r = reshuffle / x = quit): ").strip().lower()
    if choice == "x":
        print("👋 Exiting program.")
        exit()
    elif choice == "y":
        # Export to CSV
        filename = "lineup.csv"
        try:
            with open(filename, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Batting Order", "Player Name", "Initials"])
                for i, initials in enumerate(lineup, start=1):
                    writer.writerow([i, players_dict[initials], initials])
            print(f"\n📄 Lineup saved to '{filename}' successfully.")
        except Exception as e:
            print(f"⚠️ Failed to write CSV: {e}")
        break
    elif choice == "r":
        continue  # reshuffle
    else:
        print("❌ Invalid input. Please enter 'y', 'r', or 'x'.")
