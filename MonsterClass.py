class Monster:
    def __init__(self, monster_name=None, hp=None, intelligence=None, charisma=None, strength=None, wisdom=None,
                 dexterity=None, constitution=None, ac=None, speed=None, damage_resistances=None, damage_immunities=None,
                 cr=None, size=None, alignment=None, condition_immunities=None, number_of_dice=None, type_of_dice=None):
        self.monster_name = monster_name
        self.hp = hp
        self.intelligence = intelligence
        self.charisma = charisma
        self.strength = strength
        self.wisdom = wisdom
        self.dexterity = dexterity
        self.constitution = constitution
        self.ac = ac
        self.speed = speed
        self.damage_resistances = damage_resistances
        self.damage_immunities = damage_immunities
        self.cr = cr
        self.size = size
        self.alignment = alignment
        self.condition_immunities = condition_immunities
        self.number_of_dice = number_of_dice
        self.type_of_dice = type_of_dice

    def getmonstername(self):
        return self.monster_name

    def setmonstername(self, monster_name):
        self.monster_name = monster_name

    def getintelligence(self):
        return self.intelligence

    def setintelligence(self, intelligence):
        self.intelligence = intelligence

    def getcharisma(self):
        return self.charisma

    def setcharisma(self, charisma):
        self.charisma = charisma

    def getstrength(self):
        return self.strength

    def setstrength(self, strength):
        self.strength = strength

    def getwisdom(self):
        return self.wisdom

    def setwisdom(self, wisdom):
        self.wisdom = wisdom

    def getdextarity(self):
        return self.dexterity

    def setdexterity(self, dexterity):
        self.dexterity = dexterity

    def getconsitution(self):
        return self.constitution

    def setconsitution(self, constitution):
        self.constitution = constitution

    def getac(self):
        return self.ac

    def setac(self, ac):
        self.ac = ac

    def gethp(self):
        return self.hp

    def sethp(self, hp):
        self.hp = hp

    def getspeed(self):
        return self.speed

    def setspeed(self, speed):
        self.speed = speed

    def getdamageresistances(self):
        return self.damage_resistances

    def setdamageresistances(self, damage_resistances):
        self.damage_resistances = damage_resistances

    def getdamageimmunities(self):
        return self.damage_immunities

    def setdamageimmunities(self, damage_immunities):
        self.damage_immunities = damage_immunities

    def getcr(self):
        return self.cr

    def setcr(self, cr):
        self.cr = cr

    def getsize(self):
        return self.size

    def setsize(self, size):
        self.size = size

    def getalignment(self):
        return self.alignment

    def setalignment(self, alignment):
        self.alignment = alignment

    def getconditionimmunities(self):
        return self.condition_immunities

    def setconditionimmunities(self, condition_immunities):
        self.condition_immunities = condition_immunities

    def getnumberofdice(self):
        return self.number_of_dice

    def setnumberofdice(self, number_of_dice):
        self.number_of_dice = number_of_dice

    def gettypeofdice(self):
        return self.type_of_dice

    def settypeofdice(self, type_of_dice):
        self.type_of_dice = type_of_dice