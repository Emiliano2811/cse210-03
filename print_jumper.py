def print_jumper():
    line1 = ("          ___   ")
    line2 = ("        / ___ \ ")
    line3 = ("        \     / ")
    line4 = ("         \   /  ")
    line5 = ("           0    ") #if statement right here
    line_dead = ("           X    ") 
    line6 = ("          /|\   ")
    line7 = ("          / \   ")

    jumper_tries = [line1, line2, line3, line4, line5,line6, line7]
    jumper_dead = [line_dead, line6, line7]
    print(*jumper_tries, sep= "\n")

    while True: 
        press_number = int(input("press a number:"))
        if press_number == 2:
            jumper_tries.pop(0)
            tries = int((len(jumper_tries))) 
            print(*jumper_tries, sep= "\n")
            if tries == 3:
                print("you loose")
                print(*jumper_dead, sep= "\n")
                break
            else: 
                pass 

        else: 
            print(*jumper_tries, sep= "\n")

print_jumper()