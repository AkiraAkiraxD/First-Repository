import time

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
        time.sleep(0.2)
        temp+=1
    print(slide_1)
def start():
    slide_1 = " "

    temp = 0
    while temp < 100:
        print(slide_1)
        temp+=1

start()
animation()
print("Testing Commit From VSCode")

print("Slideshow Done")