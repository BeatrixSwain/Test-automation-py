# :) <3
import uuid
import random
from worldModel  import ItemCreation

def createUid():
     return uuid.uuid4().hex

def createPowerLvl():
    return random.randint(0, 10000)

def createListCreatures():
    listCreatures = []

    azrael = createCreature("Azrael", "Arcangel", "Shadows")
    if(azrael!=None):
        listCreatures.append(azrael)

    lucifer = createCreature("Lucifer", "Arcangel", "Fire")
    if(lucifer!=None):
        listCreatures.append(lucifer)

    lanna = createCreature("Lanna", "Demon", "Mystic")
    if(lanna!=None):
        listCreatures.append(lanna)

    siaxhya = createCreature("Siaxhya", "Demon", "Terra")
    if(siaxhya!=None):
        listCreatures.append(siaxhya)

    lilith = createCreature("Lilith", "Demon", "Snakes, control")
    if(lilith!=None):
        listCreatures.append(lilith)

    remiel = createCreature("Remiel", "Arcangel", "Light")
    if(remiel!=None):
        listCreatures.append(remiel)

    sariel = createCreature("Sariel", "Arcangel", "MentalControl")
    if(azrael!=None):
        listCreatures.append(sariel)

    miguel = createCreature("Miguel", "Arcangel", "Command")
    if(miguel!=None):
        listCreatures.append(miguel)

    gabriel = createCreature("Gabriel", "Arcangel", "Speed")
    if(gabriel!=None):
        listCreatures.append(gabriel)

    zadkiel = createCreature("Zadkiel", "Arcangel", "Wind")
    if(zadkiel!=None):
        listCreatures.append(zadkiel)

    return listCreatures

def createCreature(name, breed, element):
    try:
        power = createPowerLvl();
        if power < 100:
            return None
        else:
            #name, powerNum, breed, uid, element
            uid = createUid()
            return ItemCreation(name, power, breed, uid, element)
    except Exception as ex:
        print(f"Exception: {ex}")
        return None