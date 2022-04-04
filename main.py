from battlefield import Battlefield
from robot import Robot
from dinosaur import Dinosaur
jarvis = Robot("Jarvis")
rex = Dinosaur("Rex", 21)
Battlefield.run_game(jarvis, rex)


