# Rewriting the terminal-based game after execution state reset
import random
import time

class Player:
    def __init__(self, name, industry):
        self.name = name
        self.industry = industry
        self.reputation = 50  # Percentage
        self.market_share = 0  # Percentage
        self.suspicion = 0  # Percentage
        self.capital = 100000  # USD
        self.revenue = 0  # USD
        self.awareness = 0  # Percentage
        self.products = []  # List of developed products

    def balance_sheet(self):
        return f"Capital: ${self.capital}, Revenue: ${self.revenue}, Reputation: {self.reputation}%, Market Share: {self.market_share}%, Suspicion: {self.suspicion}%, Awareness: {self.awareness}%"

class Product:
    def __init__(self, name, investment, success_chance):
        self.name = name
        self.investment = investment
        self.success_chance = success_chance
        self.launched = False

class Game:
    def __init__(self):
        self.player = None
        self.opponent = None
        self.turn = 1

    def create_players(self):
        name = input("Enter your name: ")
        print("Choose your industry:")
        print("1. Tech\n2. Healthcare\n3. Automotive")
        industry_choice = input("Enter 1, 2, or 3: ")
        industries = {1: "Tech", 2: "Healthcare", 3: "Automotive"}
        industry = industries.get(int(industry_choice), "Tech")

        self.player = Player(name, industry)
        self.opponent = Player("Opponent", random.choice(["Tech", "Healthcare", "Automotive"]))

    def market_research(self):
        print("Conducting market research...")
        time.sleep(1)
        demand = random.randint(20, 100)
        supply = random.randint(20, 100)
        print(f"Market research results: Demand = {demand}%, Supply = {supply}%")
        return demand, supply

    def r_and_d(self):
        product_name = f"Product-{len(self.player.products) + 1}"
        investment = int(input(f"Enter investment amount for {product_name} (min $10,000): "))
        if investment < 10000:
            print("Minimum investment is $10,000!")
            return

        success_chance = min(50 + (investment // 1000), 95)
        product = Product(product_name, investment, success_chance)
        self.player.products.append(product)
        self.player.capital -= investment
        print(f"Developed {product_name} with {success_chance}% success chance.")

    def launch_product(self, product):
        if product.launched:
            print(f"{product.name} is already launched!")
            return

        print(f"Launching {product.name}...")
        time.sleep(1)
        if random.randint(1, 100) <= product.success_chance:
            self.player.revenue += product.investment * 1.5
            self.player.market_share += random.randint(5, 10)
            self.player.awareness += random.randint(5, 10)
            product.launched = True
            print(f"{product.name} launched successfully! Revenue increased.")
        else:
            print(f"{product.name} launch failed. Better luck next time.")

    def marketing(self):
        investment = int(input("Enter marketing investment amount: "))
        if investment > self.player.capital:
            print("Not enough capital!")
            return

        effectiveness = random.randint(1, 100)
        self.player.capital -= investment
        self.player.awareness += min(effectiveness // 10, 100 - self.player.awareness)
        self.player.reputation += random.randint(1, 5)
        self.player.revenue += investment * (effectiveness / 100)
        print("Marketing campaign successful!")

    def hacking(self):
        print("Hacking opponent...")
        time.sleep(1)
        if random.randint(1, 100) <= 50:  # 50% success rate
            self.opponent.reputation -= random.randint(5, 15)
            self.opponent.revenue -= random.randint(5000, 20000)
            self.player.suspicion += random.randint(10, 25)
            print("Hacking successful! Opponent reputation and revenue decreased.")
        else:
            self.player.suspicion += 20
            print("Hacking failed! Suspicion increased.")

    def random_event(self):
        events = [
            "Industry scrutiny! Suspicion for all players increased by 10%.",
            "Product ban! One of your products has been banned, reducing revenue.",
            "Economic boom! Capital and revenue increased by $20,000.",
            "Tax increase! All players lose $10,000 from capital."
        ]
        event = random.choice(events)
        print(f"Random Event: {event}")
        if "scrutiny" in event:
            self.player.suspicion += 10
            self.opponent.suspicion += 10
        elif "ban" in event and self.player.products:
            banned_product = random.choice(self.player.products)
            self.player.products.remove(banned_product)
            self.player.revenue -= 10000
            print(f"Banned {banned_product.name}!")
        elif "boom" in event:
            self.player.capital += 20000
            self.player.revenue += 20000
        elif "tax" in event:
            self.player.capital -= 10000
            self.opponent.capital -= 10000

    def check_game_over(self):
        if self.player.suspicion >= 100:
            print("Suspicion reached 100%! Government shuts down your company.")
            return True
        if self.player.reputation <= 0:
            print("Reputation dropped to 0%! Public boycott destroyed your company.")
            return True
        if self.player.market_share >= 100:
            print("Congratulations! You achieved 100% market share and won the game!")
            return True
        if self.player.capital <= 0:
            print("Capital depleted! You are bankrupt.")
            return True
        return False

    def play_turn(self):
        print(f"\n--- Turn {self.turn} ---")
        print(self.player.balance_sheet())
        print("Available actions:")
        print("1. Market Research")
        print("2. R&D")
        print("3. Launch Product")
        print("4. Marketing")
        print("5. Hacking")
        print("6. Skip Turn")

        try:
            choice = int(input("Choose your action (1-6): "))
            if choice == 1:
                self.market_research()
            elif choice == 2:
                self.r_and_d()
            elif choice == 3:
                if not self.player.products:
                    print("No products to launch!")
                else:
                    for i, product in enumerate(self.player.products):
                        print(f"{i + 1}. {product.name} (Success Chance: {product.success_chance}%)")
                    prod_choice = int(input("Choose a product to launch: ")) - 1
                    if 0 <= prod_choice < len(self.player.products):
                        self.launch_product(self.player.products[prod_choice])
                    else:
                        print("Invalid choice!")
            elif choice == 4:
                self.marketing()
            elif choice == 5:
                self.hacking()
            elif choice == 6:
                print("Turn skipped.")
            else:
                print("Invalid action!")
        except ValueError:
            print("Invalid input! Turn skipped.")

        self.random_event()
        if self.check_game_over():
            return True
        self.turn += 1
        return False

    def start_game(self):
        self.create_players()
        print("\nGame Start!")
        while True:
            if self.play_turn():
                break


# Start the game
game = Game()
game.start_game()
