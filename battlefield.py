from robot import Robot
from dinosaur import Dinosaur
jarvis = Robot("Jarvis")
rex = Dinosaur("Rex", 21)

class Battlefield:
    def __init__(self):
        self.robot = jarvis
        self.dinosaur = rex
    def run_game(self):
        Battlefield.display_welcome(self)
        Battlefield.battle_phase(self)
        Battlefield.display_winner(self)
    
    def display_welcome(self):

        print(f"Welcome {self.robot.name} and {self.dinosaur.name} to the arena!")

    def battle_phase(self):
        keep_fighting = True
        while keep_fighting == True:
            if self.robot.health <= 0 or self.dinosaur.health <= 0:
                keep_fighting = False
            else:
                self.robot.attack_random_weapon(self.dinosaur)
                print(F"{self.robot.name} has attacked {self.dinosaur.name}, {self.dinosaur.name} has {self.dinosaur.health} health remaining.")
                if self.dinosaur.health <=0:
                    break
                self.dinosaur.attack(self.robot)
                print(F"{self.dinosaur.name} has attacked {self.robot.name}, {self.robot.name} has {self.robot.health} health remaining.")

            
    def display_winner(self):
        if self.dinosaur.health <= 0:
            print(f"{self.robot.name} has won the fight!")
        elif self.robot.health <= 0:
            print(f"{self.dinosaur.name} has won the fight!")


    def run_game_herd_and_fleet(fleet_list, herd_list):
        Battlefield.display_welcome_herd_and_fleet(fleet_list, herd_list)
        Battlefield.battle_phase(fleet_list, herd_list)
        Battlefield.display_winner(fleet_list,herd_list)

    def display_welcome_herd_and_fleet(robot, dinosaur):
        print(f"Welcome {robot.name} and {dinosaur.name} to the arena!")