#-----------------------------------------------------------
# Title: Rpg map and inventory
# Class: CS 30
# Date: March 25, 2023
# Coders Name: Deepash Sunwar
# Version: 3
#-----------------------------------------------------------
'''
Current Assignment: rpg map and inventory

This program has database of rooms the user can go to, it allows user to quit anytime, it is continous play.
'''

import database

# all the action the user can do after walking into a room
after_movement = ["back", "search", "quit"]

# from the map it takes all the directions and stores it in this list
room_direction = [direc[1]['action_key'] for direc in database.map]

# this var lets me check which actions are valid and not depending on where the user is at
in_room = False

# empty inventory
inventory = []

# this var allows me to check which rooms they've already collected items from
searched_rooms = {}

# the starting room
current_location = "The bedroom"


def line_break():
  """
    creates a sort of 'line' break, only for user to see easily
    """
  print("\n===================================\n")


def display_movement():
  """
    Displays the movements(and room) the user could take(north, west, south, east)
    """
  for i in range(len(database.map)):
    print(
      f"({database.map[i][1]['action_key'].capitalize()}) {database.map[i][0]}"
    )
  print("(map) Print map")
  print("(Inventory)")
  print("(Quit)")


def movement_actions():
  """
    takes in user input for what action they would want to do
    """
  return input("What action would you like to do: ").lower()


def location_description(location):
  """
    it prints the user's location description
    """
  print("LOCATION DESCRIPTION:")
  for i in range(len(database.map)):
    if database.map[i][0] == location:
      print(database.map[i][1]['description'])


def take_object(item):
  """
    It puts items user finds in the inventory
    """
  inventory.append(item)


def print_inventory():
  """
    It prints out the user's inventory
    """
  print("Your current inventory: ")
  for i in range(len(inventory)):
    print(inventory[i])


def object_description(item):
  """
    it prints out the object's description
    """
  print(database.objects[item]['object_description'])


def possible_movements():
  """
    It prints out all the possible movements the user can make after they have entered a room
    """
  global after_movement
  print("Only possible movements: ")
  for i in range(len(after_movement)):
    print(f"({after_movement[i].capitalize()})")


def search(location):
  """
    It searches the room they are in for an object, then it takes the     object out of the dictonary and returns the name of it
    """
  global searched_rooms
  if location in searched_rooms:
    print("You've already grabbed the object from this room!")
    line_break()
  for key in database.objects:
    if location == database.objects[key]['room_name']:
      print("OBJECT FOUND!")
      print(
        f"You have found a {key} and it has been stored into your inventory!")
      line_break()
      print("OBJECT DESCRIPTION: ")
      object_description(key)
      line_break()
      database.objects.pop(key)
      searched_rooms[location] = True
      return key
  return None


def print_map():
  data = ""
  for i in range(len(database.map)):
    data = data + database.map[i][0] + " is in the " + \
        database.map[i][1]['action_key'] + "\n"
  try:
    with open('map.txt', 'r') as f:
      print(f.read())
  except FileNotFoundError:
    with open('map.txt', 'w') as f:
      f.write(data)
      print(data)


while True:

  # Keeps track of where user is
  print(f"current location: {current_location}")
  line_break()

  # if the user is at starting room
  if current_location == "The bedroom":
    display_movement()
    line_break()

  # if the user is not at starting room
  else:
    possible_movements()
    line_break()

  # asks for user input
  user_action_choice = movement_actions()
  line_break()

  # checks if the user input is within the possible directions
  if user_action_choice in room_direction:

    # checks if they are in a room that is not the starting room
    if in_room and current_location != "The bedroom":
      print("Please enter a valid movement!")
      line_break()

      continue
    # if they aren't then it prints out the possible directions they can go to
    for i in range(len(database.map)):
      if user_action_choice == database.map[i][1]['action_key']:
        current_location = database.map[i][0]
        location_description(current_location)
        in_room = True
        break

  # checks if the user wants to quit
  if user_action_choice == "quit":
    print("Thank you for playing!")
    break
  # checks if user wants to search
  elif user_action_choice == "search" and current_location != "The bedroom":
    object = search(current_location)
    if object != None:
      take_object(object)

  # checks if user wants to access inventory
  elif user_action_choice == "inventory":
    print_inventory()
    line_break()
    continue

  elif user_action_choice == "map":
    print_map()
    line_break()
    continue

  # checks if the user wants to go to main menu
  elif user_action_choice == "back":
    current_location = "The bedroom"
    continue

  # if the user input does not equal to any of the possible actions then it gives them a invalid message
  else:
    print("Please enter a valid action!")
    line_break()
    continue

print(database.map[0][0])
print(database.map[0][1]['action_key'])
