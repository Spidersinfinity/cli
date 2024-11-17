# Rewriting the terminal-based game after execution state reset
import random
import time

#Player Class
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
    

class Game:
    def __init__(self):
        self.player = None
        self.opponent = None
        self.turn = 1

    
    def create_players(self):
        name1 = input("Enter name for player 1: ")
        print("Choose your industry:")
        print("1. Tech\n2. Healthcare\n3. Automotive")
        industry_choice1 = input("Enter 1, 2, or 3: ")


        name2 = input("Enter name for player 1: ")
        print("Choose your industry:")
        print("1. Tech\n2. Healthcare\n3. Automotive")
        industry_choice2 = input("Enter 1, 2, or 3: ")

        industries = {1: "Tech", 2: "Healthcare", 3: "Automotive"}
      

        self.player = Player(name1, industries.get(int(industry_choice1))
        self.opponent = Player(name2, industries.get(int(industry_choice2)))

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
