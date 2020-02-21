# Write a class to hold player information, e.g. what room they are in
# currently.
class Player: 
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.inventory = []

    def printInventory(self):
        print(" You check your bag and find:")
        if(self.inventory and len(self.inventory) > 0):
            for i in self.inventory:
                print(i)
        else: 
            print("   //Nothing.")
    
    def addItem(self, item):
        self.inventory.append(item)

    def removeItem(self, item):
        self.inventory.remove(item)
        