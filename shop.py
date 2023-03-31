
class Weapon: #무기상
    def __init__(self, name, power):
        self.name = name
        self.power = power        

class Knife:
    def __init__(self):
        self.item_name = "검"
        self.power = 5
        self.price = 450

class OldCam:
    def __init__(self):
        self.item_name = "낡은 캠"
        self.power = 30
        self.price = 2500

class Keyboard:
    def __init__(self):
        self.item_name = "키보드-no.59"
        self.power = 200
        self.price = 10000
