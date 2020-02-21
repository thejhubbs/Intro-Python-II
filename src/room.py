# Implement a class to hold room information. This should have name and
# description attributes.
class Room: 
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f"| {self.name} | \n-{self.description}-"

    def printItems(self):
        print(self)
        print(" You look around and see:")
        if(len(self.items) > 0):
            for i in self.items:
                print(i)
        else: 
            print("   //Nothing.")

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)
        