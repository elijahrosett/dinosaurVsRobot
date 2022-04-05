from dinosaur import Dinosaur
rex = Dinosaur("Rex", 21)
tom = Dinosaur("Tom", 12)
jim = Dinosaur("Jim", 5)
dan = Dinosaur("dan", 17)
herd_list = [tom, jim, dan, rex]
class Herd:
    def __init__(self, herd_name, herd_list):
        self.name = herd_name
        self.health = []
        self.attack = sum([])

    def herd_health(list):
        for item in list:
            heard_health_list.append(item.health)
        return 

dino_herd = Herd("Dino Herd", herd_list)
