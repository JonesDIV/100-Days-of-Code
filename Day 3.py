#initial learning from begining of the lesson
#print("Welcome to the rollercoaster!\nWe have to check if you are tall enough to ride. \nEnter you're height below.")
#height = int(input("Enter Height in cm:\n"))
#if height > 120:
#    print("You can ride the rollercoaster!")
#    age = int(input("What is your age? "))
#    if age >= 18:
#      print("Your ticket costs $17")
#    else:
#      print("Your ticket costs $8")
#else:
#    print("Sorry, we cannot let you on this ride.")

#number = int(input("Type a number: "))
#if number % 2 == 0:
#   print("This is an even number")
#else:
#  print("This is an odd number")

#Create a Tresure hunt game
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to the Treasure hunt!")
print("Answer the questions to find the hidden secrets on this island!\nThe options will be the last mentioned, it is case sensitive.")
print("You are in the middle of the ocean after your expedition ship sunk.\nYou can either swim to find shore or float on a plank of wood from the wreckage.")

question_a = input("What do you do? Swim or Float?\n")
if question_a == "Swim":
    print("You quickly find shore and soon you are on a beautiful beach. There is a dense jungle to your left and the wreckage scattered on the beach to the right")
    print("You can either search along the beach or discover what is in the jungle")
    question_c = input("What do you do? Beach or Jungle?\n")
    if question_c == "Beach":
        print("You discover a map amongst the wreckage! Observing your surroundings, it looks like this could be the island you were looking for!")
        print("You see a clear direction in the jungle that would direct you to a cave.")
        print("You can either follow the map and investigate the cave, or stay on the beach in hopes someone will come and rescue you.")
        question_d = input("What do you do? Follow or Stay?\n")
        if question_d == "Follow":
            print("It doesn't take long, soon you are in the cave.\nYou are presented with three gems; Blue, Green and Red. The map has a drawing of a green gem, this must mean something")
            print("You can either pick up the green gem or just see what happens if you pick up another gem.")
            question_e = input("Which colour do you pick up? Red, Green or Blue?\n")
            if question_e == "Green":
                print("The floor trembles as the door opens and inside all the treasures imaginable lay before you. You are rich!")
                print("You win the game!")
            elif question_e == "Red":
                print("You feel and sting in your neck and pull out a dart. You lose your vision and fall to the floor as you have been poisoned.")
                print("Game Over")
            else:
                print("The floor rumbled, but not in a good way.\nYou look up to see a giant boulder falling from the sky where you are standing.")
                print("Game Over")
        else:
            print("You wait on the shore in the hopes of rescue.")
            print("In the distance you see a small paddle boat. You recoginse some of the passengers, they're your crew members!")
            print("They join you on the island and asking if you have discovered the treasure. You could share with them your discovery or fight them off to take the treasure for yourself")
            question_g = input("What do you do? Share or Fight?\n")
            if question_g == "Share":
                print("You share the map with the crew and you decide to find the treasure together.")
                print("It doesn't take long, soon you are all in the cave.\nYou are presented with three gems; Blue, Green and Red. The map has a drawing of a green gem, this must mean something")
                print("You can either pick up the green gem or just see what happens if you pick up another gem.")
                question_e = input("Which colour do you pick up? Red, Green or Blue?\n")
                if question_e == "Green":
                    print("The floor trembles as the door opens and inside all the treasures imaginable lay before you. You are all rich!")
                    print("You win the game!")
                elif question_e == "Red":
                    print("You feel and sting in your neck and pull out a dart.\nYou lose your vision and fall to the floor as you have been poisoned. The rest of the crew fall to the same fate")
                    print("Game Over")
                else:
                    print("The floor rumbled, but not in a good way.\nYou all look up to see a giant boulder falling from the sky where you are all standing.")
                    print("Game Over")
            else:
                print("You choose to fight")
                print("Unfortunately, you were never the strongest fighter and easily apprehended.")
                print("Game Over")
    else:
        print("The Jungle is dense, but you are determined. It all pays off when you find a cave, this will do for shelter.")
        print("Upon entering the cave, you dicover three gems in front of what looks like a door")
        print("The colours of the gems are Blue, Green and Red. You have a sense that one of these gems will trigger the door")
        question_f = input("Which colour do you pick? Blue, Green or Red?\n")
        if question_f == "Green":
            print("The floor trembles as the door opens and inside all the treasures imaginable lay before you. You are rich!")
            print("You win the game!")
        elif question_f == "Red":
            print("You feel and sting in your neck and pull out a dart. You lose your vision and fall to the floor as you have been poisoned.")
            print("Game Over")
        else:
            print("The floor rumbled, but not in a good way.\nYou look up to see a giant boulder falling from the sky where you are standing.")
            print("Game Over")
else:
    print("The plank of wood holds you safely on the ocean.\nIt is starting to get hot under the sun and you are hungry")
    print("You have two choices, either fish in the ocean or try paddling the plank to shore.")
    question_h = input("What do you do? Paddle or Fish?\n")
    if question_h == "Paddle":
        print("You quickly find shore and soon you are on a beautiful beach. There is a dense jungle to your left and the wreckage scattered on the beach to the right")
        print("You can either search along the beach or discover what is in the jungle")
        question_c = input("What do you do? Beach or Jungle?\n")
        if question_c == "Beach":
            print("You discover a map amongst the wreckage! Observing your surroundings, it looks like this could be the island you were looking for!")
            print("You see a clear direction in the jungle that would direct you to a cave.")
            print("You can either follow the map and investigate the cave, or stay on the beach in hopes someone will come and rescue you.")
            question_d = input("What do you do? Follow or Stay?\n")
            if question_d == "Follow":
                print("It doesn't take long, soon you are in the cave.\nYou are presented with three gems; Blue, Green and Red. The map has a drawing of a green gem, this must mean something")
                print("You can either pick up the green gem or just see what happens if you pick up another gem.")
                question_e = input("Which colour do you pick up? Red, Green or Blue?\n")
                if question_e == "Green":
                    print("The floor trembles as the door opens and inside all the treasures imaginable lay before you. You are rich!")
                    print("You win the game!")
                elif question_e == "Red":
                    print("You feel and sting in your neck and pull out a dart. You lose your vision and fall to the floor as you have been poisoned.")
                    print("Game Over")
                else:
                    print("The floor rumbled, but not in a good way.\nYou look up to see a giant boulder falling from the sky where you are standing.")
                    print("Game Over")
            else:
                print("You wait on the shore in the hopes of rescue.")
                print("In the distance you see a small paddle boat. You recoginse some of the passengers, they're your crew members!")
                print("They join you on the island and asking if you have discovered the treasure. You could share with them your discovery or fight them off to take the treasure for yourself")
                question_g = input("What do you do? Share or Fight?\n")
                if question_g == "Share":
                    print("You share the map with the crew and you decide to find the treasure together.")
                    print("It doesn't take long, soon you are all in the cave.\nYou are presented with three gems; Blue, Green and Red. The map has a drawing of a green gem, this must mean something")
                    print("You can either pick up the green gem or just see what happens if you pick up another gem.")
                    question_e = input("Which colour do you pick up? Red, Green or Blue?\n")
                    if question_e == "Green":
                        print("The floor trembles as the door opens and inside all the treasures imaginable lay before you. You are all rich!")
                        print("You win the game!")
                    elif question_e == "Red":
                        print("You feel and sting in your neck and pull out a dart.\nYou lose your vision and fall to the floor as you have been poisoned. The rest of the crew fall to the same fate")
                        print("Game Over")
                    else:
                        print("The floor rumbled, but not in a good way.\nYou all look up to see a giant boulder falling from the sky where you are all standing.")
                        print("Game Over")
                else:
                    print("You choose to fight")
                    print("Unfortunately, you were never the strongest fighter and easily apprehended.")
                    print("Game Over")
        else:
            print("The Jungle is dense, but you are determined. It all pays off when you find a cave, this will do for shelter.")
            print("Upon entering the cave, you dicover three gems in front of what looks like a door")
            print("The colours of the gems are Blue, Green and Red. You have a sense that one of these gems will trigger the door")
            question_f = input("Which colour do you pick? Blue, Green or Red?\n")
            if question_f == "Green":
                print("The floor trembles as the door opens and inside all the treasures imaginable lay before you. You are rich!")
                print("You win the game!")
            elif question_f == "Red":
                print("You feel and sting in your neck and pull out a dart. You lose your vision and fall to the floor as you have been poisoned.")
                print("Game Over")
            else:
                print("The floor rumbled, but not in a good way.\nYou look up to see a giant boulder falling from the sky where you are standing.")
                print("Game Over")
    else:
        print("You managed to capture a fish! You try cooking it by creating a flickering flame you made from kindling floating by")
        print("The fish is barely cooked and you get food poisoning.")
        print("Game Over")