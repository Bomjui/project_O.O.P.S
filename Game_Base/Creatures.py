from Text import creatures_names, city_place_distance
from Helpy import dijkstara_with_path, get_exact_path
import Text as txt
import Helpy as hlp
import curses
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


print(list(creatures_names.keys()))
Police = Creatures("Police", creatures_names["police"][0], creatures_names["police"][1], creatures_names["police"][2],
                   creatures_names["police"][3])
Trained_police = Creatures("Trained_police", creatures_names["Trained_police"][0], creatures_names["Trained_police"][1], creatures_names["Trained_police"][2],
                   creatures_names["Trained_police"][3])
Soldier = Creatures("Soldier", creatures_names["Soldier"][0], creatures_names["Soldier"][1], creatures_names["Soldier"][2],
                   creatures_names["Soldier"][3])
Special_soldier = Creatures("Special_soldier", creatures_names["Special_soldier"][0], creatures_names["Special_soldier"][1], creatures_names["Special_soldier"][2],
                   creatures_names["Special_soldier"][3])
O_O_P_E_R_S = Creatures("O.O.P.E.R.S", creatures_names["O.O.P.E.R.S"][0], creatures_names["O.O.P.E.R.S"][1], creatures_names["O.O.P.E.R.S"][2],
                   creatures_names["O.O.P.E.R.S"][3])
target = "sector_2c"
distances, predecessors = dijkstara_with_path(city_place_distance, "Your_base")
path = get_exact_path(predecessors, "Your_base", target)
print(f"Кратчайшее расстояние: {distances.get(target)}")
print(f"Mаршрут: {' -> '.join(path)}")
print(path)
city_distance = curses.wrapper(lambda stdscr: hlp.city_distances(stdscr, txt.city_places, 0, 1, path,
                                True, "---[City plan]------------------------------------------------------------------------------"))

print(city_distance)