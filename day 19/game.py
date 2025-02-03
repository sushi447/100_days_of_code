import sys
print ("Hello. Do you want to play a game?")
if input() in ("yes", "yeah", "YEAH", "Yes", "sure"):
    print("Okay, great!")
else:
    print ("Goodbye.")
    sys.exit()
print("Well, if you really want to play, let's get started!")
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
    print("Sure. The story begins.")
    print("You wake up and find yourself in a dark cave, and you hear rumbling noises. What do you do?")
    print(" You can choose to walk around and explore, or pretend nothing is happening and go back to sleep?")
else:
    print("Well, that's too bad.")
    sys.exit()
