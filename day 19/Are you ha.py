print("Hello from vscode")

while True:
    for x in range(5):
        print("you better be hapy!")
    print("Are you hapy?")
    if input() in ("yes","Yes","YES","yeah","Yeah","YEAH"):
        print("Awesome! Amazing! Extraodrinary! Super! Bye!")
        for y in range(5):
            print("Bye!")
        print("Didn't you hear me? I said bye! Now get out!")
        break
    else: 
        print("Let's try this again!  :)")
