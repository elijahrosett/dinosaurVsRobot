from robot import Robot
from dinosaur import Dinosaur


class Battlefield:
    def __init__(self, robot, dinosaur):
        self.robot = robot
        self.dinosaur = dinosaur

    def run_game(robot, dinosaur):
        Battlefield.display_welcome(robot, dinosaur)
        Battlefield.battle_phase(robot, dinosaur)
        Battlefield.display_winner(robot,dinosaur)
    
    def display_welcome(robot, dinosaur):
        print(f"Welcome {robot.name} and {dinosaur.name} to the arena!")

    def battle_phase(robot, dinosaur):
        keep_fighting = True
        while keep_fighting == True:
            if robot.health <= 0 or dinosaur.health <= 0:
                keep_fighting = False
            else:
                robot.attack_random_weapon(dinosaur)
                print(F"{robot.name} has attacked {dinosaur.name}, {dinosaur.name} has {dinosaur.health} health remaining.")
                dinosaur.attack(robot)
                print(F"{dinosaur.name} has attacked {robot.name}, {robot.name} has {robot.health} health remaining.")

        

        
    def display_winner(robot, dinosaur):
        if dinosaur.health <= 0:
            print(f"{robot.name} has won the fight!")
        elif robot.health <= 0:
            print(f"{dinosaur.name} has won the fight!")

