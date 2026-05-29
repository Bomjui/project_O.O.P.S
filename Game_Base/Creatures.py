
class Creatures:
    def __init__(self, name, hp, speed, attack, armor):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.attack_damage = attack
        self.armor = armor

    def take_damage(self, enemy):
        if self.armor > 0:
            self.hp = (self.hp + self.armor) - enemy.attack_damage
        else:
            self.hp = self.hp - enemy.attack_damage
        if self.hp <= 0:
            print(f"{self.name} death")
        else:
            print(f"{self.name}: {self.hp} hp")

    def attack(self, enemy):
        print(f"{self.name} attack {enemy.name} - {self.attack_damage} hp")
        enemy.take_damage(self)


class Soldiers(Creatures):
    def __init__(self, name, hp, speed, attack, armor):
        super().__init__(name, hp, speed, attack, armor)


Police = Creatures("Police", 100, 10, 500, 0)
BoB = Creatures("BoB", 100, 5, 10, 10)
Police.attack(BoB)

