from character import Character

class Monster(Character):
    def __init__(self):
        super().__init__()  # Calls parent constructor
        print(f"Monster created with Combat Strength: {self.combat_strength} and Health: {self.health_points}")

    def monster_attacks(self, hero):
        print(f"Monster attacks with {self.combat_strength} damage!")
        hero.health_points -= self.combat_strength
        if hero.health_points <= 0:
            print("Monster has defeated the hero!")

    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector")
        super().__del__()  # Calls parent destructor
