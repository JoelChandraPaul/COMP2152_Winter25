from character import Character

class Hero(Character):
    def __init__(self):
        super().__init__()  # Calls parent constructor
        print(f"Hero created with Combat Strength: {self.combat_strength} and Health: {self.health_points}")

    def hero_attacks(self, monster):
        print(f"Hero attacks with {self.combat_strength} damage!")
        monster.health_points -= self.combat_strength
        if monster.health_points <= 0:
            print("Hero has defeated the monster!")

    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector")
        super().__del__()  # Calls parent destructor
