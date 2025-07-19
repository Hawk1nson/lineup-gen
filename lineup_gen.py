import random

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

# Prompt for unavailable players
all_players = list(players_dict.keys())

# try statement for number of players
all_players = list(players_dict.keys())  # Keep this line above

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
                break  # Go to next player

    # Remove those players from the lineup
    active_players = [p for p in all_players if p not in not_playing]
    break  # Exit the input loop and move on

# Validate function
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

# Generate and print
lineup = generate_valid_lineup(active_players, forbidden_pairs)

if lineup:
    print("\n✅ Valid Batting Lineup:")
    for i, initials in enumerate(lineup, start=1):
        print(f"{i}. {players_dict[initials]} ({initials})")
else:
    print("❌ Could not generate a valid lineup after many attempts.")
