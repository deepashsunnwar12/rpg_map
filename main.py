#-----------------------------------------------------------
# Created by: Deepash Sunwar
# Created date: 09/16/23
# version = "2.0"
#-----------------------------------------------------------

# The map databse includes all information about a specific room
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


# creates a line break by calling this function (easier to see information)
def line_break():
  print("\n-------------------------------\n")


# global var for starting room
current_location = "The bedroom"

# the bedroom description
print(
  "You are in a small bedroom, containing a simple bed, a dresser, and a window. The air is still and quiet, and the room feels cozy and safe."
)

line_break()

# the game loop
while True:
  # This prints out the current location the user is at
  print(f"current location: {current_location}")
  line_break()

  # print all the available locations and a quit option if current location is not the start room
  if current_location == "The bedroom":
    for i in range(len(map)):
      print(f"({map[i][1]['action_key'].capitalize()}) {map[i][0]}")
    print("(Quit) Quit")

  # if the current location is not the bedroom then the only option for user is to go back to bedroom or quit

  else:
    print("Only possible movements: ")
    print("  ")
    print("(back) The bedroom")
    print("(Quit) Quit")

  line_break()

  # asks the user what location they want to explore
  user_location_choice = input(
    "Which location do you want to explore: ").lower()

  line_break()
  # checks if user wants to quit
  if user_location_choice == "quit":
    print("Thank you for playing!")
    break

  # also checks if the user wants to go back to the start room
  elif user_location_choice == "back":
    current_location = "The bedroom"
    continue

  # this checks if the movement is valid( at first is false)
  valid_movement = False

  # checks what the user wanted to explore and prints out description
  for i in range(len(map)):
    if user_location_choice == map[i][1]['action_key']:
      print("LOCATION DESCRIPTION:")
      print("  ")
      print(map[i][1]['description'])
      current_location = map[i][0]
      valid_movement = True  # movement becomes true here because the user input was valid
      break

  # if the input was not valid it restarts the loop
  if not valid_movement:
    print("You did not enter a valid movement")
    continue
