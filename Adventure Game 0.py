import time
import random


def single_item(out_list, in_list):
    index = 0

    while len(in_list) < 9:
        item1 = random.choice(out_list)

        for no in (in_list[index: index + 1]):
            if item1 in in_list:
                break

            else:
                in_list.append(item1)
                index += 1

    return(in_list)


def real_keys(inlist1, inlist2, key1, key2,
              key3, key4, key5, key6, key7, key8, Keys_help):

    key1.append("1")
    key1.append(inlist1[1])
    key1.append(inlist2[1])

    key2.append("2")
    key2.append(inlist1[2])
    key2.append(inlist2[2])

    key3.append("3")
    key3.append(inlist1[3])
    key3.append(inlist2[3])

    key4.append("4")
    key4.append(inlist1[4])
    key4.append(inlist2[4])

    key5.append("5")
    key5.append(inlist1[5])
    key5.append(inlist2[5])

    key6.append("6")
    key6.append(inlist1[6])
    key6.append(inlist2[6])

    key7.append("7")
    key7.append(inlist1[7])
    key7.append(inlist2[7])

    key8.append("8")
    key8.append(inlist1[8])
    key8.append(inlist2[8])

    Keys_help.append("1")
    Keys_help.append(inlist1[1])
    Keys_help.append(inlist2[1])

    Keys_help.append("2")
    Keys_help.append(inlist1[2])
    Keys_help.append(inlist2[2])

    Keys_help.append("3")
    Keys_help.append(inlist1[3])
    Keys_help.append(inlist2[3])

    Keys_help.append("4")
    Keys_help.append(inlist1[4])
    Keys_help.append(inlist2[4])

    Keys_help.append("5")
    Keys_help.append(inlist1[5])
    Keys_help.append(inlist2[5])

    Keys_help.append("6")
    Keys_help.append(inlist1[6])
    Keys_help.append(inlist2[6])

    Keys_help.append("7")
    Keys_help.append(inlist1[7])
    Keys_help.append(inlist2[7])

    Keys_help.append("8")
    Keys_help.append(inlist1[8])
    Keys_help.append(inlist2[8])


def text_split(answer, list_out):

    x = answer.split()
    for item in x:
        list_out.append(item)


def valid_input(answer, the_list, answer1, Keys_help, true_key, key1,
                key2, key3, key4, key5, key6, key7, key8,
                inventory, items, drain, colors, clothes):

    while True:
        answer = input(answer).lower()
        text_split(answer, answer1)

        if set(answer1).isdisjoint(the_list):
            print_pause("probaly the fall messed up with your head." +
                        " What you want makes no sense")
            game(Keys_help, true_key, key1, key2, key3, key4,
                 key5, key6, key7, key8, inventory, answer1, items,
                 drain, colors, clothes)

        else:

            break
        return answer

    return answer


def print_pause(phrase_to_print):
    print(phrase_to_print)
    time.sleep(1.5)


def draining(drain, inventory):

    drain.append("+1")

    if len(drain) == 1:
        print_pause("Something in this whole procedure" +
                    " makes you feal drained," +
                    " as if a part of you" +
                    " remains with the tunel each time you make the passage.")

    if len(drain) == 2:
        print_pause("Something in this whole procedure" +
                    " makes you feal drained," +
                    " as if a part of you" +
                    " remains with the tunnel each time you make the passage.")
        print_pause("You eyesight plays weird games with you. " +
                    "You see things that aren't there," +
                    " movement in the margins of your vision")

    if len(drain) == 3:
        print_pause("Something in this whole procedure" +
                    " makes you feal drained," +
                    " as if a part of you" +
                    " remains with the tunnel each time you make the passage.")
        print_pause("You start feeling num")
        print_pause("You eyesight plays weird games with you." +
                    "You see things that aren't there," +
                    " movement in the margins of your vision")
        print_pause("Strings of energy," +
                    " or a blur that takes strangely meaningful forms")

    if len(drain) == 4:
        print_pause("Something about all this makes you feal drained," +
                    " as if a part of you" +
                    " remains with the tunnel each time you make the passage.")
        print_pause("You eyesight plays weird games with you." +
                    "You see things that aren't there," +
                    " movement in the margins of your vision")
        print_pause("You start feeling num")
        print_pause("Last time, was just the fall you found difficult;" +
                    " this time it was standing up as well.")
        print_pause("And then you see her. Can it be?")
        print_pause("Is this happening. " +
                    "Is this really a woman extending her hand to you?")

        while True:

            proposal = input("Will you take her hand? Y/N").lower()

            if 'yes' in proposal or 'y' in proposal:
                print_pause("You take her hand. " +
                            "Within this place" +
                            " if feels strangely warm and substantial," +
                            " even thought it seems formed of blue energy.")
                print_pause("The woman smiles at you" +
                            " and with a explosive move," +
                            " you wouldn’t be able to dodge it anyhow," +
                            " she stabs you with something," +
                            " just at the height of your heard.")
                print_pause("You feel no pain," +
                            " just a strange joy," +
                            " and the feeling that you are whole again.")
                print_pause("when you exit this place" +
                            " you will find something new in you possession.")
                inventory.append("second_half_mirror")
                break

            elif 'no' in proposal or 'n' in proposal:
                print_pause("What madness is this, madness or treachery. " +
                            "None of both a thing you need right now. " +
                            "You are not taking her hand.")
                break

            else:
                print_pause("This whole thing," +
                            " has probably messed up with your head. " +
                            "I do not know what you mean.")

    if len(drain) == 5:

        print_pause("Something in all this makes you feal drained," +
                    " as if a part of you remains" +
                    " with the tunnel each time you make the passage.")
        print_pause("You eyesight plays weird games with you. " +
                    "You see things that aren't there," +
                    " movement in the margins of your vision")
        print_pause("You know that this time" +
                    " you might not be able to stand up after falling," +
                    " or trying again the passage")
        print_pause("And then you see her. Can it be?")
        print_pause("Is this happening. " +
                    "Is this really a woman extending her hand to you?")

        while "second_half_mirror" not in inventory:

            proposal = input("Will you take her hand? Y/N").lower()

            if 'yes' in proposal or 'y' in proposal:
                print_pause("You take her hand. " +
                            "Within this place" +
                            " if feels strangely warm and substantial," +
                            " thought it seems formed of blue energy.")
                print_pause("The woman smiles at you and," +
                            " with a explosive move," +
                            " you wouldn’t be able to dodge it anyhow," +
                            " she stabs you with something," +
                            " just at the height of your heard.")
                print_pause("You feel no pain," +
                            " just a strange joy," +
                            " and the feeling that you are whole again.")
                print_pause("when you exit here," +
                            " you will find something new in you possession.")
                inventory.append("second_half_mirror")
                break

            elif 'no' in proposal or 'n' in proposal:
                print_pause("What madness is this, madness or treachery. " +
                            "None of both a thing you need right now. " +
                            "You are not taking her hand.")
                break

            else:
                print_pause("This whole experience" +
                            " has probably messed up with your head. " +
                            "I do not know what you mean.")

    if len(drain) == 6:
        print_pause("This time," +
                    " you know it is going to be the last one")
        print_pause("You are feeling," +
                    " that you are about to die.")
        print_pause("The woman extend her hand" +
                    " for the last time.")
        print_pause("She seems sad.")

        while "second_half_mirror" not in inventory:

            proposal = input("Will you take her hand? Y/N").lower()

            if 'yes' in proposal or 'y' in proposal:
                print_pause("You take her hand. " +
                            "Within this place" +
                            " if feels strangely warm" +
                            " and strangely substantial," +
                            " even thought it is formed of blue energy.")
                print_pause("The woman smiles at you" +
                            " and with a explosive move," +
                            " you wouldn’t be able to dodge anyhow," +
                            " she stabs you with something," +
                            " just at the height of your heard.")
                print_pause("You feel no pain, just a strange joy," +
                            " and the feeling that you are whole again.")
                print_pause("when you exit here," +
                            " you will find something new in you possession.")
                inventory.append("second_half_mirror")
                break

            elif 'no' in proposal or 'n' in proposal:
                print_pause("What madness is this, madness or treachery. " +
                            "None of both a thing you need right now. " +
                            "You are not taking her hand.")
                break

            else:
                print_pause("This whole experience" +
                            " has probably messed up with your head. " +
                            "I do not know what you mean.")


def intro(Keys_help, true_key, key1, key2, key3,
          key4, key5, key6, key7, key8,
          inventory, answer1, items, drain,
          colors, clothes):

    print_pause("\nYou found this place" +
                " exactly where the map said it would be")
    print_pause("Trough the altar," +
                " in the derelict chapel, on the mountain top")
    print_pause(" and then," +
                " through the caves, you found the tunels,"
                " as you were supposed to")
    print_pause("This was the tome all right")
    print_pause(" you cheered then,")
    print_pause(" and now," +
                " through all the traps and riddles you are here,")
    print_pause(" in the last room, where the actual tomp is and...")
    main(Keys_help, true_key, key1, key2, key3,
         key4, key5, key6, key7, key8,
         inventory, answer1, items, drain,
         colors, clothes)


def main(Keys_help, true_key, key1, key2, key3,
         key4, key5, key6, key7, key8, inventory,
         answer1, items, drain, colors,
         clothes):

    print_pause("\n...you know that something is wrong" +
                " in a moment.\n")
    print_pause("As the half mirror," +
                " taken by your friend,")
    print_pause(" is being released" +
                " from the grip of a metallic hand" +
                " in the altar with a ‘click’")
    print_pause(" all happen at once.\n")

    print_pause("The creature is formed out of nothing.")
    print_pause("All becomes green smoke, ash," +
                " and the smell of death.")
    print_pause("And as it lashes against your friends," +
                " you feel a pull and...")
    print_pause(" all is lost.\n")

    print_pause("Completely disoriented" +
                " you are being sucked through a tunnel" +
                " of blue bright light,")
    loop(Keys_help, true_key, key1, key2, key3,
         key4, key5, key6, key7, key8, inventory,
         answer1, items, drain, colors,
         clothes)


def passing():

    print_pause("You take a deep breath" +
                " and step through the gate")
    print_pause("Immediately you feel" +
                " the same sensation of being sucked")
    print_pause("You enter and start traveling through the same," +
                " or a very similar-looking tunnel again")


def passing2(drain, inventory, answer1, Keys_help, true_key, key1, key2, key3,
             key4, key5, key6, key7, key8, items,
             colors, clothes):
    print_pause("At some point," +
                " you see the end in front.")
    print_pause("And the exit seems" +
                " to be getting bigger and bigger")
    print_pause("you reach it and with a sudden pause" +
                " of the force pushing you until now... ")
    if len(drain) > 6:
        drained_ending(answer1, Keys_help, true_key, key1, key2, key3,
                       key4, key5, key6, key7, key8, inventory, items,
                       drain, colors, clothes)


def loop(Keys_help, true_key, key1, key2, key3,
         key4, key5, key6, key7, key8, inventory, answer1, items,
         drain, colors, clothes):

    print_pause("you are thrown," +
                " after what seemed to be an eternity,")
    print_pause("into the middle of a small," +
                " ancient-looking room.\n")

    print_pause("Here, with you is a man.")
    print_pause("He looks fragile and old, barely standing.")
    print_pause("There are many strange things on him," +
                " but what draws your attention more" +
                f" is a '{random.choice(colors)}' {random.choice(clothes)}")
    print_pause("and a black belt with the banner of Good Talos on it\n")

    print_pause("All-around the room stand tall doors," +
                " that are radiating bright light, that hurts your eyes.")
    print_pause("You can’t see where they lead.\n")

    print_pause("As the man is politely waiting for you to stand back up")
    print_pause("You count eight doors in total," +
                " including the one you just were thrown out of.")
    print_pause("In front of each one of the doors," +
                " are short columns with a pillow on top.")
    print_pause("On top of each pilow a strange items is laid.\n")

    print_pause("The man speaks to you.\n")
    print_pause("'Not a very smart idea, was it?'")
    print_pause("'To rob my tomp, I mean.'\n")
    print_pause("'And now here you are, my prisoner in this time loop," +
                " for all eternity")
    print_pause("Unless you are willing to make a deal, that is.'\n")
    print_pause("'I will let you go, but " +
                " first you will give me the most valuable thing you have.'")

    bargain(Keys_help, true_key, key1, key2, key3,
            key4, key5, key6, key7, key8, inventory,
            answer1, items, drain, colors,
            clothes)


def bargain(Keys_help, true_key, key1, key2, key3,
            key4, key5, key6, key7, key8, inventory,
            answer1, items, drain, colors,
            clothes):
    while True:
        answer = input("'If you agree say 'yes'" +
                       " if you do not say 'no'\n").lower()

        if 'yes' in answer or 'y' in answer:

            print_pause("His polite smile disappears." +
                        " He stares you in the eye intently.")
            print_pause("As you return the stare," +
                        " you think that his eyes are progressively darkened" +
                        " -as if becoming dark holes.")
            print_pause("and that his smile is substituted" +
                        " by something that lightens him up in a worrisome," +
                        " eery way.")
            print_pause("by the grin of a predator" +
                        " that is just about to strike\n")

            print_pause("Are you certain?")
            print_pause("After this there is no coming back")

            answer2 = input("Please, choose if you are going to" +
                            " say 'yes' or 'no' whisely. \n").lower()

            while True:
                if 'yes' in answer2 or 'y' in answer2:
                    print_pause("The man bursts into a maniacal laughter," +
                                " that threatens to throw him down")
                    print_pause("You think that in between the laughter" +
                                " you hear him saying 'so be it, then'")
                    print_pause("but you can’t be certain")
                    print_pause("Immediately you get sucked" +
                                " through another tunnel")
                    last_circle()
                    bad_ending(answer1, Keys_help, true_key, key1, key2,
                               key3, key4, key5, key6, key7, key8,
                               inventory, items, drain, colors,
                               clothes)

                elif 'no' in answer2 or 'n' in answer2:
                    disappointment(Keys_help, true_key, key1, key2, key3,
                                   key4, key5, key6, key7, key8, inventory,
                                   answer1, items, drain, colors,
                                   clothes)

                else:
                    print_pause("probaly your fall messed up with your head." +
                                " What you want makes no sense")

        elif 'no' in answer or 'n' in answer:
            disappointment(Keys_help, true_key, key1, key2, key3,
                           key4, key5, key6, key7, key8, inventory,
                           answer1, items, drain, colors,
                           clothes)

        else:
            print_pause("probaly the fall messed up with your head." +
                        " What you want makes no sense")

    return answer


def game_intro(Keys_help, true_key, key1, key2, key3,
               key4, key5, key6, key7, key8, inventory,
               answer1, items, drain, colors,
               clothes):

    print_pause("\n'In this case," +
                " there is only one choice remaining!'\n")

    print_pause("The man says happily.\n")

    print_pause("'We will play the Game!'\n")

    print_pause("'To exit here.'")
    print_pause("'One of those items is the key.'")
    print_pause("'Take it and step through the door" +
                " in front of it.'\n")

    print_pause("'If you are lucky you can win.'")
    print_pause("'But you should know," +
                " there is a price to be paid it's time you try'\n")

    print_pause("'If your luck runs out, who knows...'")
    print_pause("'In the end," +
                " I might get what I lust for after all'\n")
    game(Keys_help, true_key, key1, key2, key3,
         key4, key5, key6, key7, key8, inventory,
         answer1, items, drain, colors, clothes)


def game(Keys_help, true_key, key1, key2, key3,
         key4, key5, key6, key7, key8, inventory,
         answer1, items, drain, colors, clothes):

    while True:
        print_pause("The items are: ")
        print_pause(' ' + (' '.join(key1)) + ',' +
                    ' ' + (' '.join(key2)) + ',' +
                    ' ' + (' '.join(key3)))
        print_pause(' ' + (' '.join(key4)) + ',' +
                    ' ' + (' '.join(key5)) + ',' +
                    ' ' + (' '.join(key6)))
        print_pause(' ' + (' '.join(key7)) + ',' +
                    ' ' + (' '.join(key8) + '\n'))

        if "second_half_mirror" in inventory:

            print_pause("The man seems briefly" +
                        " to be slightly bothered by something.")
            print_pause("As if somehow," +
                        " something feels a bit different.")
            print_pause("He seems not to be able to pin it down though.")

            print_pause("As you fall you feel on your sight" +
                        " something under your vest," +
                        " something that was not there before.")
            print_pause("Pretending that you are just trying to stand up," +
                        " you feel its form.")
            print_pause("It is a semicircle.")
            print_pause("Would it be to bold to think that" +
                        " it must be the other half of the mirror" +
                        " from the tome?")
            print_pause("But how?")

            while True:
                answer5 = input("Will you take it out to see? Y/N\n")

                if 'yes' in answer5 or 'y' in answer5:

                    print_pause("With all the strength that you can master" +
                                " you take it out.")
                    print_pause("The other half of the mirror it is indeed.")
                    print_pause("The man sees it," +
                                " but is somehow unable to" +
                                " prosses this information.")
                    print_pause("As if the item does not register for him.")
                    print_pause("As you look," +
                                " you see something that" +
                                " should not be there reflected on it.")
                    print_pause("It is the…")
                    print_pause(true_key)
                    break

                if 'no' in answer5 or 'n' in answer5:
                    print_pause("Much to cautious to react," +
                                " you decide that it would probably be" +
                                " a better idea to play along" +
                                " according to the given rules.")
                    break

                else:
                    print_pause("The whole experience has" +
                                " probably messed up with your head." +
                                " I do not know what you mean.")

        answer = valid_input("The man smiles and" +
                             " waits for your move." +
                             " What will you choose?\n",
                             Keys_help, answer1, Keys_help,
                             true_key, key1, key2, key3, key4,
                             key5, key6, key7, key8,
                             inventory, items, drain, colors,
                             clothes).lower()

        for item in answer1:

            if item in items:
                your_key = item

            elif item == '1':
                point = 1
                your_key = Keys_help[point + 1: point + 2]
            elif item == '2':
                point = 4
                your_key = Keys_help[point + 1: point + 2]
            elif item == '3':
                point = 7
                your_key = Keys_help[point + 1: point + 2]
            elif item == '4':
                point = 10
                your_key = Keys_help[point + 1: point + 2]
            elif item == '5':
                point = 13
                your_key = Keys_help[point + 1: point + 2]
            elif item == '6':
                point = 16
                your_key = Keys_help[point + 1: point + 2]
            elif item == '7':
                point = 19
                your_key = Keys_help[point + 1: point + 2]
            elif item == '8':
                point = 22
                your_key = Keys_help[point + 1: point + 2]

        if set(answer1).isdisjoint(Keys_help) is False:
            print_pause("\nCautiously you extend your hand" +
                        f" and grab the {your_key}.\n")

            if set(answer1).isdisjoint(true_key) is False:
                print_pause("Your hand pulsates with a slight warmth," +
                            " like if holding a heart. \n")

                while True:
                    answer2 = input("Now you have a key." +
                                    " Will you enter the gate?" +
                                    " ype 'yes' or 'no'\n").lower()

                    if 'yes' in answer2 or 'y' in answer2:
                        passing()
                        passing2(drain, inventory, answer1, Keys_help,
                                 true_key, key1, key2, key3,
                                 key4, key5, key6, key7, key8,
                                 items, colors, clothes)
                        last_circle()
                        good_ending(answer1, Keys_help, true_key,
                                    key1, key2, key3, key4, key5, key6, key7,
                                    key8, inventory, items, drain,
                                    colors, clothes)

                    elif 'attack' in answer2 or 'sword' in answer2:
                        print_pause("you step forward and" +
                                    " attack the wizard with your sword")
                        print_pause("but your slice finds only ear")
                        print_pause("you step back" +
                                    " to see the wizard still standing," +
                                    " excatly at the same spot")
                        print_pause("The man smiles and waits for your move." +
                                    " What will you do next? \n")

                    elif 'no' in answer2 or 'n' in answer2:
                        while True:

                            answer4 = input("would you like to choose" +
                                            " a different item" +
                                            " or enter the Gate?" +
                                            " Yes/Enter \n").lower()

                            if 'yes' in answer4 or 'y' in answer4:
                                answer1[:] = []
                                game(Keys_help, true_key, key1, key2,
                                     key3, key4, key5, key6, key7, key8,
                                     inventory, answer1, items, drain,
                                     colors, clothes)

                            elif 'enter' or 'gate' in answer4:
                                passing()
                                passing2(drain, inventory, answer1,
                                         Keys_help, true_key, key1, key2, key3,
                                         key4, key5, key6, key7, key8,
                                         items, colors, clothes)
                                last_circle()
                                good_ending(answer1, Keys_help, true_key, key1,
                                            key2, key3, key4, key5, key6, key7,
                                            key8, inventory, items,
                                            drain, colors, clothes)

                            elif 'attack' in answer4 or 'sword' in answer4:
                                print_pause("you step forward and attack" +
                                            " the wizard with your sword")
                                print_pause("but your slice finds only ear")
                                print_pause("you step back to see the wizard" +
                                            " still standing," +
                                            " excatly at the same spot")
                                print_pause("The man smiles and" +
                                            " waits for your move." +
                                            " What will you do next? \n")

                            else:
                                print_pause("The man smiles and waits" +
                                            " for your move." +
                                            " What will you do next? \n")

                        return answer4
                    return answer4
                return answer4

            if set(answer1).isdisjoint(true_key):

                while True:
                    answer2 = input("Now you have a key." +
                                    " Will you enter the gate?" +
                                    " Type 'yes' or 'no'\n").lower()

                    if 'yes' in answer2 or 'y' in answer2:

                        answer1[:] = []
                        passing()
                        draining(drain, inventory)
                        passing2(drain, inventory, answer1, Keys_help,
                                 true_key, key1, key2, key3, key4, key5,
                                 key6, key7, key8, items, colors,
                                 clothes)
                        loop(Keys_help, true_key, key1, key2, key3,
                             key4, key5, key6, key7, key8, inventory,
                             answer1, items, drain, colors,
                             clothes)

                    elif 'attack' in answer2 or 'sword' in answer2:
                        print_pause("you step forward and" +
                                    " attack the wizard with your sword")
                        print_pause("but your slice finds only ear")
                        print_pause("you step back" +
                                    " to see the wizard still standing," +
                                    " excatly at the same spot")
                        print_pause("The man smiles and waits for your move." +
                                    " What will you do next? \n")

                    if 'no' in answer2 or 'n' in answer2:
                        while True:

                            answer4 = input("would you like to choose" +
                                            " a different item or" +
                                            " enter the Gate?" +
                                            " Yes/Enter \n").lower()

                            if 'yes' in answer4 or 'y' in answer4:
                                answer1[:] = []
                                game(Keys_help, true_key, key1, key2,
                                     key3, key4, key5, key6, key7, key8,
                                     inventory, answer1,
                                     items, drain, colors,
                                     clothes)

                            elif 'enter' or 'gate' in answer4:
                                answer1[:] = []
                                passing()
                                draining(drain, inventory)
                                passing2(drain, inventory, answer1,
                                         Keys_help, true_key, key1,
                                         key2, key3, key4,
                                         key5, key6, key7, key8,
                                         items, colors,
                                         clothes)
                                loop(Keys_help, true_key, key1, key2, key3,
                                     key4, key5, key6, key7, key8, inventory,
                                     answer1, items, drain, colors, clothes)

                            elif 'attack' in answer4 or 'sword' in answer4:
                                answer1[:] = []
                                print_pause("you step forward and" +
                                            " attack the wizard" +
                                            " with your sword")
                                print_pause("but your slice finds only ear")
                                print_pause("you step back" +
                                            " to see the wizard" +
                                            " still standing," +
                                            " excatly at the same spot")
                                print_pause("The man smiles and" +
                                            " waits for your move." +
                                            " What will you do next? \n")

                            else:
                                print_pause("The man smiles and" +
                                            " waits for your move." +
                                            " What will you do next? \n")

                        return answer4
                    return answer2
                return answer2
            return answer2
        return answer
    return answer


def disappointment(Keys_help, true_key, key1, key2,
                   key3, key4, key5, key6, key7, key8, inventory,
                   answer1, items, drain, colors,
                   clothes):

    print_pause("The man’s face returns" +
                " to smiling politely")
    print_pause("'This is a bit disappointing of course,")
    print_pause("but I can’t say that I don’t understand'")

    game_intro(Keys_help, true_key, key1, key2,
               key3, key4, key5, key6, key7, key8,
               inventory, answer1, items,
               drain, colors, clothes)


def last_circle():

    print_pause("You step into the same room you came from.")
    print_pause("You are back within the tomp.")
    print_pause("You see your friend.")
    print_pause("He is still alive.")
    print_pause("He and the creature are at the exact same place.")
    print_pause("As if not a single moment has passed" +
                " since you entered the tunnel for the first time.")
    print_pause("You raise your sword and strike.")
    print_pause("You take the creature by surprise" +
                " and kill it with a single swift strike.")
    print_pause("As its scream still echoes in the ancient room," +
                " you turn to look at your friend.")


def bad_ending(answer1, Keys_help, true_key, key1, key2,
               key3, key4, key5, key6, key7, key8, inventory,
               items, drain, colors, clothes):

    print_pause("\nHe turns at you, but" +
                " right away you know that something is wrong\n")
    print_pause("He scream, he drops the half mirror and runs away")
    print_pause("As his scream draws further and further away,")
    print_pause("You look yourself in" +
                " the half mirror on the ground...\n")
    print_pause(" ...and you see a transformation" +
                " developing in front of your own eyes\n")
    print_pause("What was once your face" +
                " is now being changing into something else.")
    print_pause("In its place start appearing the features of an old man" +
                " with slightly demented gaze")
    print_pause("The original terror you felt" +
                " gives its place to the numbness of despair")
    print_pause("and then, this," +
                " gives its place to the surprising urge," +
                " to laugh.\n")
    print_pause("To laugh and to keep laughing until the world dies\n")
    print_pause("And why not? This is a day to celebrate." +
                " Because after so many years, finally...\n")
    print_pause("\nYOU HAVE RETURNED!\n")
    end(answer1, Keys_help, true_key, key1, key2,
        key3, key4, key5, key6, key7, key8, inventory,
        items, drain, colors, clothes)


def drained_ending(answer1, Keys_help, true_key, key1, key2,
                   key3, key4, key5, key6, key7, key8, inventory,
                   items, drain, colors, clothes):

    print_pause("You fall in the middle of the chamber.")
    print_pause("You vision is blurry.")
    print_pause("You turn your head up to see the man.")
    print_pause("He seems to be standing at the exact same place.\n")
    print_pause("His characteristics are not clear.")
    print_pause("Not even the colors are clear anymore.")
    print_pause("All seems to be green.")
    print_pause("There is a sound though,")
    print_pause("That sound that as all start seeming odd,")
    print_pause("You think that you can recognize.")
    print_pause("Yes, the sound is a laughter,")
    print_pause("A wild hysterical laughter\n")

    print_pause("You feel yourself getting lighter.")
    print_pause("The point of your vision is being raised up,")
    print_pause("But it is not you who is doing this.")
    print_pause("You even doubt if it is even you the person who watches.\n")

    print_pause("The man speaks to you.")
    print_pause("You don’t know what he says.")
    print_pause("But you need to obey.")
    print_pause("You turn and you look at your hands…\n")

    print_pause("All green smoky mist and dust.")

    print_pause("\nForm afar you hear the screams" +
                " of your dying friend.\n")
    end(answer1, Keys_help, true_key, key1, key2, key3,
        key4, key5, key6, key7, key8, inventory,
        items, drain, colors, clothes)


def good_ending(answer1, Keys_help, true_key, key1, key2,
                key3, key4, key5, key6, key7, key8, inventory,
                items, drain, colors, clothes):

    print_pause("\nHe turns at you," +
                " and then at the creature that is now" +
                " dissolving fast into thin air\n")
    print_pause("He smiles and thanks you for saving his life")
    print_pause("'This place is creeping me out," +
                " let’s get out of here' he says")
    print_pause("You agree," +
                " but something tells you to turn and" +
                "look a particular wall," +
                " through the mirror\n")
    print_pause("You have no idea why" +
                "you want to do that," +
                " but you do it anyway.")
    print_pause("From within the mirror" +
                " the wall appear not to be a wall at all,")
    print_pause("but rather a room full of leather bags" +
                " of gold and gems.")
    print_pause("You show this to your friend" +
                " and both of your faces lighten up\n")
    print_pause("This was not such a waste of time after all")
    print_pause("\nYOU RETURN HOME WITH THE TREASURE!\n")
    end(answer1, Keys_help, true_key, key1, key2, key3,
        key4, key5, key6, key7, key8, inventory, items,
        drain, colors, clothes)


def end(answer1, Keys_help, true_key, key1, key2,
        key3, key4, key5, key6, key7, key8,
        inventory, items, drain, colors,
        clothes):

    print_pause("This was my game.")
    print_pause("Thank you for playing")

    while True:
        restart = input("Would you like to play again?\n" +
                        " If yes type 'y' or 'yes' ;" +
                        " If no, type 'no' or 'n'\n").lower()

        if 'yes' in restart or 'y' in restart:
            answer1[:] = []
            inventory[:] = []
            intro(Keys_help, true_key, key1, key2, key3,
                  key4, key5, key6, key7, key8, inventory,
                  answer1, items, drain, colors,
                  clothes)
        elif 'no' in restart or 'n' in restart:
            print_pause("Thank you again")
            print_pause("Good Bye")
            Keys_help[:] = []
            exit()

        else:
            print_pause("I don't know what this is.")

    return restart


def play():
    drain = []
    items = ["stone", "bone", "orb", "feather",
             "dagger", "bottle", "amulet", "pin", "boot",
             "lamp", "clock", "book", "candle", "ring", "crown"]
    real_attributes = ["0"]
    inventory = []
    attributes = ["red", "green", "purple", "gold",
                  "emerald", "ruby", "wooden", "marble", "blue",
                  "triangular", "metallic", "glass"]
    real_items = ["0"]
    colors = ["red", "green", "purple", "gold",
              "emerald green", "blue", "pink", "turquoise",
              "fuchsia", "aquamarine", "maroon", "coral"]
    clothes = ["cardigan", "hat", "slipper", "robe",
               "glove", "vest", "skirt", "dress", "chain mail",
               "full plate mail", "tie"]
    key1 = []
    key2 = []
    key3 = []
    key4 = []
    key5 = []
    key6 = []
    key7 = []
    key8 = []
    keys = [key1, key2, key3, key4, key5, key6, key7, key8]
    Keys_help = []
    answer1 = []

    single_item(attributes, real_attributes)
    single_item(items, real_items)
    real_keys(real_attributes, real_items,
              key1, key2, key3,
              key4, key5, key6, key7, key8, Keys_help)
    true_key = random.choice(keys)
    intro(Keys_help, true_key, key1, key2, key3, key4,
          key5, key6, key7, key8, inventory, answer1, items,
          drain, colors, clothes)


play()
