from battlefield import Battlefield
from robot import Robot
from dinosaur import Dinosaur
jarvis = jarvis = Robot("Jarvis")
rex = Dinosaur("Rex", 17)
Battlefield.battle_phase(jarvis, rex)
print(jarvis.health)
print(rex.health)

