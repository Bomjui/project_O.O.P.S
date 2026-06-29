import asyncio
from Text import city_place_distance, creatures_names
import Helpy as hlp
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

    def speed_run(self, place):
        pass
Police = Creatures("Police", creatures_names["Police"][0], creatures_names["Police"][1], creatures_names["Police"][2],
                   creatures_names["Police"][3])
Trained_police = Creatures("Trained_police", creatures_names["Trained_police"][0], creatures_names["Trained_police"][1], creatures_names["Trained_police"][2],
                   creatures_names["Trained_police"][3])
Soldier = Creatures("Soldier", creatures_names["Soldier"][0], creatures_names["Soldier"][1], creatures_names["Soldier"][2],
                   creatures_names["Soldier"][3])
Special_soldier = Creatures("Special_soldier", creatures_names["Special_soldier"][0], creatures_names["Special_soldier"][1], creatures_names["Special_soldier"][2],
                   creatures_names["Special_soldier"][3])
O_O_P_E_R_S = Creatures("O.O.P.E.R.S", creatures_names["O.O.P.E.R.S"][0], creatures_names["O.O.P.E.R.S"][1], creatures_names["O.O.P.E.R.S"][2],
                   creatures_names["O.O.P.E.R.S"][3])
async def paths(target, creatures="", start="Your_base"):
    if creatures == "Police":
        start = "Police"
    distances, predecessors = await hlp.dijkstara_with_path(city_place_distance, start)
    path = await hlp.get_exact_path(predecessors, start, target)
    await asyncio.sleep(0.05)
    return path
async def Creatures_choice(stdscr):
   Creature_choice = await hlp.Left_window_func(stdscr).main(stdscr, list(creatures_names.keys()), 0, "Your work bench:",
                            0, 1, True)
   await asyncio.sleep(0.05)
   return Creature_choice