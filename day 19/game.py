import sys
while True:
    print ("Hello. Do you want to play a game?")
    if input() in ("yes", "yeah", "YEAH", "Yes", "sure"):
        print("Okay, great!")
        break
    else:
        print ("Let's try this again.")
print("Do you want to do a quiz or a story game?")
answer = input()
if ("quiz") in answer:
    correct = 0
    print("Sure. I can quiz you.")
    print("Who was the first president of the United States?")
    quizanswer = input()
    if ("washington" or "Washington") in quizanswer:
        correct = correct + 1
        print("Yes. Good Job.")
    else: print("How did you get this wrong?")
    print("Okay. Next question.")
    print("What is the square root of 144?")
    if input() in ("12","twelve"):
        correct = correct +1
        print("Gread job! You're smart.")
    else:
        print("You're dumb.")
    print("Okay. Next question")
    print("Who is the richest person in the world?")
    musk = input()
    if ("musk" or "elon" or "Musk") in musk:
        correct = correct +1
        print("Yay! You're tough to beat!")
    else:
        print("Oh, come on. That was so easy!")
    print("Good job! You got", correct, "correct!")
    print("It was nice talking with you. Goodbye.")
    sys.exit()
if ("story") in answer:
    while True:
        print(" ")
        print("You wake up and find yourself in a dark cave, and you hear rumbling noises. What do you do?")
        print("Option 1. You can choose to walk around and explore.")
        print("Option 2. Pretend nothing is happening and go back to sleep.")
        option = input()
        if ("2" or "second") in option:
            print("Okay. You go back to sleep and well, I don't know. You were never seen again.")
            print("Let's try this again.")
        if ("1" or "first") in option:
            break
    print(" ")
    print("Okay. You try to walk around, but it is too dark and you cannot see anything.")
    print("Being the brainless foolish person you are, you keep walking, and-")
    print("THUD!")
    print("You bump into a wall. Ouch!")
    print("Following the wall with your hand, you eventually see a small spartke of light ahead.")
    while True:
        print (" ")
        print("Determined now more than ever, you keep walking.")
        print("Or do you?")
        print(" 1. Keep walking to towards the light.")
        print(" 2. Give up, duh! I'm not made for this.")
        duh = input()
        if ("2" or "give") in duh:
            print("Guess you're just too lazy.")
            print("Let's try this again.")
        if ("1" or "walk") in duh:
            break
    print(" ")
    print("Okay. So as I was saying, more determined than ever, you keep walking.")
    print("Hard work pays off! As you walk torawds the light, it gets brighter and brighter.")
    print("Out spreads a wide forest below. You walk to the edge of the cliff and look down, terrified.")
    print("     ")
    print("You look back, at the long, endless tunnel of darkness.")
    print("You see a dark shadow slowly approaching you.")
    print(" ")
    while True:
        print(" ")
        print("A giant comes running towards you. What do you do?")
        print("1. JUMP!")
        print("2. Don't move! Let's see what happens.")
        jump = input()
        if ("2") in jump:
            print("You stare, looking at the shadow running towards you.")
            print("The giant runs to you and grabs you by the legs. He throws you so far into the woods-")
            print("and never to be seen again.")
            print(" Let's try this again.")
        if ("1") in jump:
            break
    print(" ")
    print("You prepare to jump, but just as you're about to gracefully leap off-")
    print("CRUMBLE! CRUMBLE!")
    print(" ")
    print("The rock beneath you starts to crumble.")
    print("AAAAAAAAAAAAAAH!!!")
    print("You scream, plummeting down hundreds of feet.")
    print(" ")
    print("You jolt awake. 'Am I alive?' You question to yourself.")
    print("You look around, and see you're in a cozy bedroom, sitting in a bed.")
    print("No giants.")
    print("Yay. I guess it was just a bad dream after all.")
    print(" ")
    print("😁 You win! 😁")
    print("Congratulations!🏆🏆🏆")
    sys.exit()
else:
    print("Well, that's too bad.")
    sys.exit()
