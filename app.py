#Secret Agent Adventure Game
#Edited from the template provided by Alex Hadwen-Bennett

from random import randint

#defines the rooms in the game with descriptions.
rooms={"Street":"outside the HQ",
       "Lobby":"the lobby of the HQ",
       "Lift":"the main lift",
       "1st Floor":"the first floor of the HQ"}

#defines the exits that each room has and which room the exits lead to
#optionally you can define an object that must be in the inventory in
#order to move through the exit.
exits={"Street":{"east":["Lobby"]},
       "Lobby":{"west":["Street"],"north":["Lift"]},
       "Lift":{"south":["Lobby"],"up":["1st Floor","KeyCard"]},
       "1st Floor":{"north":["Lift"]}}

#defines the objects that are present in each room.
objects={"Street":[],
       "Lobby":["WelcomeMat","KeyCard"],
       "Lift":[],
       "1st Floor":["Minion",]}

#defines objects that hide other objects and must be move to reveal them.
hidden={"WelcomeMat":"KeyCard"}

#creates an empty list to store the inventory.
inventory=[]

#outputs the details for a room including non-hidden objects.
def roomDetails(room):
    print("\nCurrent Location:",room,"-",rooms[room])
    if len(objects[room]) > 0:
        print("Objects:")
        for object in objects[room]:
            if object not in hidden.values():
                print(object)

#moves the user to another room, if it is possible to move in that direction.
def go(direction,room):
    possible=False
    if direction in exits[room]:
        if len(exits[room][direction])==1:
            possible=True
        elif len(exits[room][direction])>1:
            if exits[room][direction][1] in inventory:
                possible=True
    if possible==True:
        room=exits[room][direction][0]
        roomDetails(room)
    else:
        print("It's not currently possible to move in that direction")
    return room

#moves an object that is hiding another object.
def move(object,room):
    if object in hidden and object in objects[room]:
        print("You have moved",object,"and revealed:",hidden[object])
        del hidden[object]
    else:
        print("It isn't possible to move this object")

#allows the user to add an object to their inventory.
def collect(object,room):
    if object in objects[room]:
        inventory.append(object)
        print(object,"has been added to your inventory.")
    else:
        print("It isn't possible to add this object to your inventory.")

# added functionality - D+D Dice Roll for fighting
def d(sides):
    return randint(1, sides)

def roll(n, sides):
    return tuple(d(sides) for _ in range(n))

def fight(enemy):
    print('Calculating luck...')
    # player rolls 3 20 dice and collect value
    dice = sum(roll(3, 20))
    print('Luck: {}'.format(dice))

    if dice > 30:
        print('You quickly move to your right and punch the minion in the face.')
        print('He goes down and you find the plans in his suit pocket. Congratulations!')
        exit()
    if dice < 30:
        print('You attempt to punch the minion but trip and fall. ')
        print('The minion kicks you out of the building. Better luck next time!')
        currentRoom="Street"

#outputs the welcoming message to the user.
print("You are a secret agent and you need to steal the plans for the enemy's new weapon from their HQ.")
print("\nThe following commands are available to you:\nGO - move north, south, east, west, up or down (e.g. go north)\nMOVE - move an object (e.g. move chair)\nCOLLECT - collect an object (e.g. collect key)\nFIGHT - fight an adversary")

#sets the starting room and displays its details.
currentRoom="Street"
roomDetails(currentRoom)

#allows the user to enter a command and takes the appropriate action.
while True:
    command=input(": ")
    command=command.split()
    if command[0].lower()=="go":
        currentRoom=go(command[1].lower(),currentRoom)
    elif command[0].lower()=="move":
        move(command[1],currentRoom)
    elif command[0].lower()=="collect":
        collect(command[1],currentRoom)
    elif command[0].lower()=="fight":
        fight(command[1])
    else:
        print("I'm sorry I didn't understand that command.")
