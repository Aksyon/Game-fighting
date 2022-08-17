"""This module is a game, where two warriors hit each other
 in a random order"""

from random import choice


class Warrior:
    """Class with main logic of game"""

    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def __str__(self):
        return self.name
        
    @staticmethod 
    def fight(fighter1, fighter2):
        """Logic of game"""

        while fighter1.health > 0 and fighter2.health > 0:
            list = [fighter1, fighter2]
            randomFighter = choice(list)
            
            if randomFighter == fighter1:
                fighter2.health -= 20
                print(f'{fighter1} attacked the opponent, health of {fighter2}'
                     f'is {fighter2.health}')
                print('- - - - - - - - - - - - - - - -')
                               
            elif randomFighter == fighter2:
                fighter1.health -= 20
                print(f'{fighter2} attacked the opponent, health of {fighter1}'
                     f'is {fighter1.health}')
                print('- - - - - - - - - - - - - - - -')
                     
        if fighter1.health == 0:
            return (f'{fighter2} won. Congratulations :)')

        elif fighter2.health == 0:
            return (f'{fighter1} won. Congratulations :)')

if __name__ == '__main__':

    fighter1 = Warrior(input("Name of the first warrior:"))
    fighter2 = Warrior(input("Name of the second warrior:"))

    print(Warrior.fight(fighter1, fighter2))

