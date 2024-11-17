import random
import time

# Initialize default values
player = {
    "capital": 100000,
    "revenue": 0,
    "market_share": 0,
    "reputation": 50,
    "suspicion": 0,
    "awareness": 0,
}

opponent = {
    "capital": 100000,
    "revenue": 0,
    "market_share": 0,
    "reputation": 50,
    "suspicion": 0,
    "awareness": 0,
}

# Game conditions
WINNING_MARKET_SHARE = 100
MAX_SUSPICION = 100
MIN_REPUTATION = 0


def print_status():
    print("\n--- Current Status ---")
    print(f"Capital: ${player['capital']}")
    print(f"Revenue: ${player['revenue']}")
    print(f"Market Share: {player['market_share']}%")
    print(f"Reputation: {player['reputation']}%")
    print(f"Suspicion: {player['suspicion']}%")
    print(f"Awareness: {player['awareness']}%\n")


def random_event():
    events = [
        "Supply chain issues (decrease revenue by 10%).",
        "Government scrutiny (increase suspicion by 10%).",
        "Product ban (decrease reputation by 10%).",
        "Seasonal demand increase (increase revenue by 20%).",
        "Tax hike (decrease capital by $5000).",
    ]
    event = random.choice(events)
    print(f"Random Event: {event}")

    if "Supply chain" in event:
        player["revenue"] -= int(player["revenue"] * 0.1)
        opponent["revenue"] -= int(opponent["revenue"] * 0.1)
    elif "Government scrutiny" in event:
        player["suspicion"] += 10
        opponent["suspicion"] += 10
    elif "Product ban" in event:
        player["reputation"] -= 10
        opponent["reputation"] -= 10
    elif "Seasonal demand increase" in event:
        player["revenue"] += int(player["revenue"] * 0.2)
        opponent["revenue"] += int(opponent["revenue"] * 0.2)
    elif "Tax hike" in event:
        player["capital"] -= 5000
        opponent["capital"] -= 5000


def player_move():
    print("\n--- Choose Your Move ---")
    print("1. Mergers & Acquisitions")
    print("2. Market Research")
    print("3. Research & Development")
    print("4. Marketing")
    print("5. Hacking")
    print("6. Spread False Rumors")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        mergers_acquisitions()
    elif choice == "2":
        market_research()
    elif choice == "3":
        research_and_development()
    elif choice == "4":
        marketing()
    elif choice == "5":
        hacking()
    elif choice == "6":
        spread_false_rumors()
    else:
        print("Invalid choice. Skipping turn.")


def mergers_acquisitions():
    cost = random.randint(10000, 30000)
    if player["capital"] >= cost:
        print(f"You acquired a company for ${cost}.")
        player["capital"] -= cost
        player["market_share"] += 10
    else:
        print("Not enough capital for M&A.")


def market_research():
    cost = 5000
    if player["capital"] >= cost:
        print("Conducting market research...")
        time.sleep(2)
        data = random.choice(["High Demand", "Low Demand", "Supply Surplus"])
        print(f"Market Research Result: {data}")
        player["capital"] -= cost
    else:
        print("Not enough capital for market research.")


def research_and_development():
    cost = 20000
    if player["capital"] >= cost:
        print("Investing in R&D...")
        time.sleep(2)
        success = random.randint(0, 1)
        if success:
            print("New product developed successfully!")
            player["market_share"] += 5
            player["awareness"] += 10
        else:
            print("R&D failed. No new product.")
        player["capital"] -= cost
    else:
        print("Not enough capital for R&D.")


def marketing():
    cost = 10000
    if player["capital"] >= cost:
        print("Launching a marketing campaign...")
        time.sleep(2)
        player["reputation"] += 5
        player["awareness"] += 10
        player["capital"] -= cost
    else:
        print("Not enough capital for marketing.")


def hacking():
    cost = 20000
    if player["capital"] >= cost:
        print("Attempting to hack the opponent...")
        time.sleep(2)
        success = random.randint(0, 1)
        if success:
            print("Hacking successful! Opponent data leaked.")
            opponent["reputation"] -= 10
            opponent["suspicion"] += 10
            player["suspicion"] += 5
        else:
            print("Hacking failed. Opponent alerted.")
            player["suspicion"] += 10
        player["capital"] -= cost
    else:
        print("Not enough capital for hacking.")


def spread_false_rumors():
    cost = 5000
    if player["capital"] >= cost:
        print("Spreading false rumors about the opponent...")
        time.sleep(2)
        opponent["reputation"] -= 5
        opponent["suspicion"] += 5
        player["capital"] -= cost
    else:
        print("Not enough capital to spread rumors.")


def check_win_loss():
    if player["market_share"] >= WINNING_MARKET_SHARE:
        print("Congratulations! You have achieved 100% market share. You win!")
        return True
    elif player["suspicion"] >= MAX_SUSPICION:
        print("Your suspicion reached 100%! The government shut you down. Game over.")
        return True
    elif player["reputation"] <= MIN_REPUTATION:
        print("Your reputation reached 0%. The public boycotts your products. Game over.")
        return True
    return False


# Main game loop
def main():
    print("Welcome to CEO vs CEO!")
    turn = 1
    while True:
        print(f"\n--- Turn {turn} ---")
        print_status()
        random_event()
        player_move()
        if check_win_loss():
            break
        turn += 1


if __name__ == "__main__":
    main()
