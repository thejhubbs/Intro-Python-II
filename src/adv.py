from room import Room
from player import Player
from item import Item

item = {
    'sword': Item("Sword", "A dangerous sword."),
    'potion': Item("Potion", "A health potion."),
    'gold': Item("Gold", "A lil hunka gold."),
    'junk': Item("Junk", "Probably not worth anything."),
}

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item['junk']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item['potion']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item['sword'], item['gold']]),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Jordan', room['outside'])
print('-------NEW GAME----------')
print(f"Welcome, {player.name}")
print(' -----------------------')
print(player.currentRoom)

# Write a loop that:
while True:
    cRoom = player.currentRoom
    direction = input("Make your move. [(N)orth (S)outh (E)ast (W)est | (C)heck Room (I)nventory | (Q)uit]\n> ")

    if(direction == 'q'):
        print('//Quitting.')
        break

    if(direction == 'n'):
        if(hasattr(cRoom, 'n_to')):
            player.currentRoom = cRoom.n_to
            print(f" You chose to move north.")
            print(player.currentRoom)
        else:
            print(" You cannot move there.")
    if(direction == 's'):
        if(hasattr(cRoom, 's_to')):
            player.currentRoom = cRoom.s_to
            print(f" You chose to move south.")
            print(player.currentRoom)
        else:
            print(" You cannot move there.")
    if(direction == 'e'):
        if(hasattr(cRoom, 'e_to')):
            player.currentRoom = cRoom.e_to
            print(f" You chose to move east.")
            print(player.currentRoom)
        else:
            print(" You cannot move there.")
    if(direction == 'w'):
        if(hasattr(cRoom, 'w_to')):
            player.currentRoom = cRoom.w_to
            print(f" You chose to move west.")
            print(player.currentRoom)
        else:
            print(" You cannot move there.")

    if(direction == 'c'):
        player.currentRoom.printItems()

    if(direction == 'i'):
        player.printInventory()

    if(direction.split()[0] == 'take'):
        target = direction.split()[1]
        if( target in item ):
            print(f"Took {target}.")
            player.currentRoom.removeItem( item[target] )
            player.addItem( item[target] )
        else:
            print(" There is no item by that name.")

    if(direction.split()[0] == 'drop'):
        target = direction.split()[1]
        if( target in item ):
            print(f"Dropped {target}.")
            player.currentRoom.addItem( item[target] )
            player.removeItem( item[target] )
        else:
            print(" There is no item by that name.")
