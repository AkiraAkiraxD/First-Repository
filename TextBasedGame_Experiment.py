import time
import random

# list = [you(0),enemy(1)]
hitPoints = [50,100]
damage = [3,1,10]
charge = 0
game = 1
attacker = "you"

def ultimateCheck():
    global charge
    charge+=1
    if charge > 5:
        charge=5
def wait():
    print("Loading...")
    time.sleep(random.randint(1,2))
def reset():
    damage[0] = 3
    damage[1] = 1
def action(num):
    global charge
    wait()
    match num:
        case 1:
            switch()
            ultimateCheck()
            dice = random.randint(1,3)
            damage[0] *= dice
            hitPoints[1] -= damage[0]
            #animation()
            main()
            print("You rolled {} and dealt {} damage!" .format(dice,damage[0]))
            reset()
        case 2:
            switch()
            ultimateCheck()
            dice = random.randint(3,10)
            hitPoints[0] += dice
            if hitPoints[0] > 50:
                hitPoints[0] = 50
            main()
            print("You healed {} health!" .format(dice))
        case 3:
            if charge == 5:
                switch()
                hitPoints[1] -= damage[2]
                #animation()
                main()
                print("YOU CASTED YOUR ULTIMATE! Dealing {} damage!" .format(damage[2]))
                charge = 0
            else:
                main()
                print("Not enough charge!")
        case _:
            main()
    gameCheck()
def diffSetting(num):
    match num:
        case 1:
            hitPoints[1] *= 0.5
        case 2:
            hitPoints[1] *= 1.0
        case 3:
            hitPoints[1] *= 1.25
        case 4:
            hitPoints[1] *= 1.5
        case 5:
            hitPoints[1] *= 2.0
        case _:
            start()
def main():
    slide_1 = '''
    HP: {}          HP: {}
    |           .       /\  |
    |  O        .      /  \ |
    |------>    .     / /\ \|
    |  |        .     \ \/ /|
    | / \       .      \  / |
    |           .       \/  |
    |1 = Attack|2 = Heal|3 = Ultimate(Charge: {}/5)|''' .format(hitPoints[0],hitPoints[1],charge)
    print(slide_1)
def animation():
    slide_1 = '''
    |           .       /\  |
    |  O        .      /  \ |
    |------>    .     / /\ \|
    |  |        .     \ \/ /|
    | / \       .      \  / |
    |           .       \/  |'''
    slide_2 = '''
    |           .       /\  |
    |  O        .      /  \ |
    |   ------> .     / /\ \|
    |  |        .     \ \/ /|
    | / \       .      \  / |
    |           .       \/  |'''
    slide_3 = '''
    |           .       /\  |
    |  O        .      /  \ |
    |    . ------>    / /\ \|
    |  |        .     \ \/ /|
    | / \       .      \  / |
    |           .       \/  |'''
    slide_4 = '''
    |           .       /\  |
    |  O        .      /  \ |
    |    .    ------> / /\ \|
    |  |        .     \ \/ /|
    | / \       .      \  / |
    |           .       \/  |'''
    slide_5 = '''
    |           .       /\  |
    |  O        .      /  \ |
    |    .       -----/ /\ \|
    |  |        .     \ \/ /|
    | / \       .      \  / |
    |           .       \/  |'''
    slide_6 = '''
    |           .       /\  |
    |  O        .      /  \ |
    |    .          --/ /\ \|
    |  |        .     \ \/ /|
    | / \       .      \  / |
    |           .       \/  |'''
    slide_7 = '''
    |           .       /\  |
    |  O        .      /  \ |
    |    .            / /\ \|
    |  |        .     \ \/ /|
    | / \       .      \  / |
    |           .       \/  |'''
    
    temp = 0
    while temp < 8:
        match temp:
            case 1:
                print(slide_1)
            case 2:
                print(slide_2)
            case 3:
                print(slide_3)
            case 4:
                print(slide_4)
            case 5:
                print(slide_5)
            case 6:
                print(slide_6)
            case 7:
                print(slide_7)
        time.sleep(0.1)
        temp+=1
def start():
    slide_1 = " "
    temp = 0
    while temp < 100:
        print(slide_1)
        temp+=1
    try:
        diff = int(input('''
    |                        |
    |         HUMAN          |
    |          vs.           |
    |        DIAMOND         |
    | (enter difficulty 1-5) |
    |                        |'''))
        diffSetting(diff)
    except ValueError:
        start()
def enemyMove():
    wait()
    time.sleep(2)
    switch()
    dice = random.randint(1,5)
    damage[1] *= dice
    hitPoints[0] -= damage[1]
    main()
    print("Diamond rolled {} and dealt {} damage!" .format(dice,damage[1]))
    reset()
    gameCheck()
def switch():
    global attacker
    match attacker:
        case "you":
            attacker = "enemy"
        case "enemy":
            attacker = "you"
def gameCheck():
    global game
    if hitPoints[0] < 1:
        game = 0
        print('''
    |========================|
    |                        |
    |       YOU LOST         |
    |        reason:         |
    |     (skill issue)      |
    |                        |
    |========================|''')
    elif hitPoints[1] < 1:
        game = 0
        print('''
    |========================|
    |                        |
    |       YOU WON?         |
    |      reported:         |
    |   (suspected hacks)    |
    |                        |
    |========================|''')


#================== GAME STARTS HERE ==================
start()
main()
while game == 1:
    if attacker == "you":
        try:
            move = int(input("Action: "))
            action(move)
        except ValueError:
            main()
    elif attacker == "enemy": 
        print("Enemy's Turn")
        enemyMove()
