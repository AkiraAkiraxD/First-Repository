import time
import random

# list = [you(0),enemy(1)]
hitPoints = [50,100]
damage = [3,1]
game = 1

def reset():
    damage[0] = 3
def action(num):
    match num:
        case 1:
            dice = random.randint(1,3)
            damage[0] *= dice
            hitPoints[1] -= damage[0]
            animation()
            main()
            print("You rolled {} and dealt {} damage!" .format(dice,damage[0]))
            reset()
        case 2:
            dice = random.randint(3,10)
            hitPoints[0] += dice
            if hitPoints[0] > 50:
                hitPoints[0] = 50
            main()
            print("You healed {} health!" .format(dice))
        case 3:
            print()
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
def main():
    slide_1 = '''
    HP: {}          HP: {}
    |           .       /\  |
    |  O        .      /  \ |
    |------>    .     / /\ \|
    |  |        .     \ \/ /|
    | / \       .      \  / |
    |           .       \/  |
    /1 = Attack/2 = Heal/3 = Defend/''' .format(hitPoints[0],hitPoints[1])
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

#================== GAME STARTS HERE ==================

start()
main()

while game == 1:
    try:
        move = int(input("Action: "))
        action(move)
    except ValueError:
        main()
    
input()
    


print("Game Done")
