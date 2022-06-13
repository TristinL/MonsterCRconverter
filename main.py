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

    for attr in newarray:
        input(f"what do you want for the {attr}?")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
