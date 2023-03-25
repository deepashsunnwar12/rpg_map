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
map = [
  [
    "The kitchen", {
      "action_key":
      "west",
      "description":
      "You step into a small kitchen, containing a stove, a sink, and a few cabinets. The air is filled with the smell of baking bread or cooking soup, and you can see a small table and a few chairs in the corner",
    }
  ],
  [
    "The study room", {
      "action_key":
      "east",
      "description":
      "You step into a small study room, containing a desk, a bookshelf, and a comfortable armchair. The air is filled with the scent of old books, and you can see a few scrolls and quills scattered on the desk.",
    }
  ],
  [
    "The attic", {
      "action_key":
      "south",
      "description":
      "You step into a dusty attic, containing a few old trunks and boxes. The air is musty and stale, and you can see some old furniture and decorations from long ago.",
    }
  ],
  [
    "The backyard", {
      "action_key":
      "north",
      "description":
      "You step outside into a small backyard, containing a few trees or bushes, a patch of grass, and perhaps a small garden plot. The air is fresh and clean, and you can hear the sound of birds chirping or leaves rustling in the wind.",
    }
  ],
]

# all objects that can be found whitin the game
objects = {
  "knife": {
    "room_name":
    "The kitchen",
    "object_description":
    "A sharp, versatile kitchen knife that can be used for cutting"
  },
  "book": {
    "room_name": "The study room",
    "object_description": "A old dusty book"
  },
  "photo": {
    "room_name": "The attic",
    "object_description": "An old photo of you and your family"
  },
  "bicycle": {
    "room_name": "The backyard",
    "object_description": "shiny blue colored bicycle"
  },
}

# all the action the user can do after walking into a room
after_movement = ["back", "search", "quit"]

# from the map it takes all the directions and stores it in this list
room_direction = [direc[1]['action_key'] for direc in map]

# this var lets me check which actions are valid and not depending on where the user is at
in_room = False

# empty inventory
inventory = []

# this var allows me to check which rooms they've already collected items from
searched_rooms = {}

# the starting room
current_location = "The bedroom"
# creates a line break by calling this function (easier to see information)


def line_break():
  """
    creates a sort of 'line' break, only for user to see easily
    """
  print("\n===================================\n")


def display_movement():
  """
    Displays the movements(and room) the user could take(north, west, south, east)
    """
  for i in range(len(map)):
    print(f"({map[i][1]['action_key'].capitalize()}) {map[i][0]}")
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
  for i in range(len(map)):
    if map[i][0] == location:
      print(map[i][1]['description'])


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
  print(objects[item]['object_description'])


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
    return None
  for key in objects:
    if location == objects[key]['room_name']:
      print("OBJECT FOUND!")
      print(
        f"You have found a {key} and it has been stored into your inventory!")
      line_break()
      print("OBJECT DESCRIPTION: ")
      object_description(key)
      line_break()
      objects.pop(key)
      searched_rooms[location] = True
      return key
  return None


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
    for i in range(len(map)):
      if user_action_choice == map[i][1]['action_key']:
        current_location = map[i][0]
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
    take_object(object)

  # checks if user wants to access inventory
  elif user_action_choice == "inventory":
    print_inventory()
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
