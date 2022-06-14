# This is a sample Python script.
from MonsterClass import Monster
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    newmonster = Monster()
    newarray = []
    for attr in dir(newmonster):
        if attr.startswith("__"):
            continue
        elif attr.startswith("get"):
            continue
        elif attr.startswith("set"):
            continue
        else:
            newarray.append(attr)
            print("object has attribute %s" % attr)

    def userinput(newarray):
        for attr in newarray:
            match attr:
                case "ac":
                    newmonster.setac(input(f"what do you want for the {attr}? "))
                case "alignment":
                    newmonster.setalignment(input(f"what do you want for the {attr}? "))
                case "charisma":
                    newmonster.setcharisma(input(f"what do you want for the {attr}? "))
                case "condition_immunities":
                    newmonster.setconditionimmunities(input(f"what do you want for the {attr}? "))
                case "constitution":
                    newmonster.setconsitution(input(f"what do you want for the {attr}? "))
                case "cr":
                    newmonster.setcr(input(f"what do you want for the {attr}? "))
                case "damage_immunities":
                    newmonster.setdamageimmunities(input(f"what do you want for the {attr}? "))
                case "damage_resistances":
                    newmonster.setdamageresistances(input(f"what do you want for the {attr}? "))
                case "dexterity":
                    newmonster.setdexterity(input(f"what do you want for the {attr}? "))
                case "hp":
                    newmonster.sethp(input(f"what do you want for the {attr}? "))
                case "intelligence":
                    newmonster.setintelligence(input(f"what do you want for the {attr}? "))
                case "monster_name":
                    newmonster.setmonstername(input(f"what do you want for the {attr}? "))
                case "number_of_dice":
                    newmonster.setnumberofdice(input(f"what do you want for the {attr}? "))
                case "size":
                    newmonster.setsize(input(f"what do you want for the {attr}? "))
                case "speed":
                    newmonster.setspeed(input(f"what do you want for the {attr}? "))
                case "strength":
                    newmonster.setstrength(input(f"what do you want for the {attr}? "))
                case "type_of_dice":
                    newmonster.settypeofdice(input(f"what do you want for the {attr}? "))
                case "wisdom":
                    newmonster.setwisdom(input(f"what do you want for the {attr}? "))
    #userinput(newarray)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
