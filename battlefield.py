from robot import Robot
from dinosaur import Dinosaur
from herd import Herd
from fleet import Fleet
todd = Robot("Todd")
eugene = Robot("Eugene")
jarvis = Robot("Jarvis")
rex = Dinosaur("Rex", 21)
tom = Dinosaur("Tom", 12)
jim = Dinosaur("Jim", 5)
dan = Dinosaur("dan", 17)
herd_list = [tom, jim, dan]
herd = Herd("DINOS", herd_list)
fleet_list = [todd, eugene, jarvis]
fleet = Fleet("The Robot Fleet", fleet_list)


class Battlefield:
    def __init__(self):
        self.robot = jarvis
        self.dinosaur = rex
        self.herd = herd
        self.fleet = fleet
        self.fleet_wins = True
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
                print(F"{self.robot.name} has attacked {self.dinosaur.name} with {self.robot.active_weapon.name} for {self.robot.active_weapon.attack_power} damage!, {self.dinosaur.name} has {self.dinosaur.health} health remaining.")
                if self.dinosaur.health <=0:
                    break
                self.dinosaur.attack(self.robot)
                print(F"{self.dinosaur.name} has attacked {self.robot.name}, {self.robot.name} has {self.robot.health} health remaining.")

            
    def display_winner(self):
        if self.dinosaur.health <= 0:
            print(f"{self.robot.name} has won the fight!")
        elif self.robot.health <= 0:
            print(f"{self.dinosaur.name} has won the fight!")


    def run_game_herd_and_fleet(self):
        Battlefield.display_welcome_herd_and_fleet(self)
        Battlefield.battle_phase_herd_and_fleet(self)
        Battlefield.display_winner_fleet_and_herd(self)

    def display_welcome_herd_and_fleet(self):
        print(f"Welcome {self.herd.name} and {self.fleet.name} to the arena!")

    def battle_phase_herd_and_fleet(self):
        keep_fighting = True
        herd_count = 0
        fleet_count = 0
        
        while keep_fighting == True: 
            fleet_member = self.fleet.list[fleet_count]
            herd_member = self.herd.list[herd_count]
            fleet_member.attack_random(herd_member)
            print(F"{fleet_member.name} has attacked {herd_member.name} with a {fleet_member.active_weapon.name} for {fleet_member.active_weapon.attack_power} damage!, {herd_member.name} has {herd_member.health} health remaining.")
            herd_member.attack_random(fleet_member)
            print(F"{herd_member.name} has attacked {fleet_member.name} for {herd_member.attack_power} damage!, {fleet_member.name} has {fleet_member.health} health remaining.")
            if herd_count == len(herd_list) - 1:
                print(f"{herd.name} is all out of players!")
                keep_fighting = False
                self.fleet_wins = True
            elif fleet_count == len(fleet_list) -1:
                print(f"{fleet.name} is all out of players!")
                keep_fighting = False
                self.fleet_wins = False
            elif fleet_member.health <= 0:
                print(f"{fleet_member.name} has died!")
                fleet_count += 1
                
            elif herd_member.health <= 0:
                print(f"{herd_member.name} has died!")
                herd_count += 1
            
    def display_winner_fleet_and_herd(self):
        if self.fleet_wins == True:
            print(f"{fleet.name} has won the fight!")
        elif self.fleet_wins == False:
            print(f"{herd.name} has won the fight!")
                    
                    
               