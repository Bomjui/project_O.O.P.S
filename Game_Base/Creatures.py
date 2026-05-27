
class Creatures:
    def __init__(self, name, hp, speed, attack):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.attack_damage = attack

    def take_damage(self, enemy):
        self.hp = self.hp - self.attack_damage
        print(f"{self.name}: {self.hp} hp")

    def attack(self, enemy):
        print(f"{self.name} attack {enemy.name} - {self.attack_damage} hp")
        enemy.take_damage(self)


class Soldiers(Creatures):
    def __init__(self, name, hp, speed, attack, armor):
        super().__init__(name, hp, speed, attack)
        self.armor = armor
