class Hero:
    #class variable
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        #instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print ("membuat Hero dengan nama " + inputName)

hero1 = Hero("sniper", 100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("Franco", 1000, 5, 10)
print(Hero.jumlah)
hero3 = Hero("Atlas", 500, 15, 9)
print(Hero.jumlah)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
