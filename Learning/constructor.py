class Hero:

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

hero1 = Hero{"sniper", 100, 10, 4}
hero2 = Hero{"Franco", 1000, 5, 10}
hero3 = Hero{"Atlas", 500, 15, 9}

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
