from robot import Robot
from dinosaur import Dinosaur


class Battlefield:
    def __init__(self, robot, dinosaur):
        self.robot = robot
        self.dinosaur = dinosaur

    def run_game(self, robot, dinosaur):
        self.display_welcome(self, robot, dinosaur)
        self.battle_phase(self, robot, dinosaur)

    def display_welcome(robot, dinosaur):
        print(f"Welcome {robot.name} and {dinosaur.name} to the arena!")

    def battle_phase(robot, dinosaur):
        while robot.health and dinosaur.health > 0:
            robot.attack(dinosaur)
            print(F"{robot.name} has attacked {dinosaur.name}, {dinosaur.name} has {dinosaur.health} health remaining.")
            dinosaur.attack(robot)
            print(F"{dinosaur.name} has attacked {robot.name}, {robot.name} has {robot.health} health remaining.")
        
        

        
    def display_winner(self, robot, dinosaur):
        if dinosaur.health <= 0:
            print(f"{robot.name} has won the fight!")
        elif robot.health <= 0:
            print(f"{dinosaur.name} has won the fight!")

