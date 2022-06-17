SpellLevels = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]
SpellLevelCopy = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]


def updateSetup():  # This function adds spell slots to a specified level
    FirstBound = (int(input("What level of spell do you wish to add to?"))-1)
    SecondBound = int(input("How many slots do you have?"))
    SpellLevels[(FirstBound)][1] = SecondBound
    SpellLevelCopy[(FirstBound)][1] = SecondBound
    print(SpellLevels)


def consumeSlot():  # This function removes a spell slot when specified
    CastSpell = (int(input("What level of spell do you wish to cast?"))-1)
    if SpellLevels[(CastSpell)][1] == 0:
        print("You have no spells of that level remaining")
    else:
        SpellLevels[(CastSpell)][1] = (int(SpellLevels[(CastSpell)][1])-1)
        SpellLevelCopy[(CastSpell)][1] = (int(SpellLevelCopy[(CastSpell)][1]) - 1)
        print(SpellLevels)


def slotRestore():  # This function restores any consumed spell slots, akin to a long rest
    SpellLevels = SpellLevelCopy
    print()
    print(SpellLevels)


def inputLoop():  # This function constantly looks for input, and then runs the corresponding function
    controlKey = input()
    if controlKey == "1":
        updateSetup()
        inputLoop()
    elif controlKey == "2":
        consumeSlot()
        inputLoop()
    elif controlKey == "3":
        slotRestore()
        inputLoop()
    else:
        inputLoop()


inputLoop()
