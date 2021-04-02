import json

class NotExistItemCreation(Exception):
    pass

class ItemCreation:
    def __init__(self, name, powerNum, breed, uid, element):
        self.uid = f"XID-{uid}"
        self.name = name
        self.power = powerNum
        self.breed = breed
        self.element = element
    
    def __str__(self):
        return json.dumps(self.__dict__)

class World:
    def __init__(self, name):
        self.name = name
        self.creations = []

    def add_creation(self, creation):
        self.creations.append(creation)

    def contains_creations(self):
        return len(self.creations)>0

    def remove_creation(self, creation):
        self.creations.remove(creation)
    
    def get_creation(self, creation):
         if creation not in self.creations:
            raise NotExistItemCreation('Item does not exist')
         return self.creations[self.creations.index(creation)]

    def getTotalPower(self):
        return sum([item.power for item in self.creations])

    def getTotalCreations(self):
        return len(self.creations)
    