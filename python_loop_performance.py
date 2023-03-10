import time

def start():
    print('''Welcome to Experiment 5!''')
    loopInput = int(input("Choose what kind of loop you want to use [1=ForLoop/2=WhileLoop]: "))
    intInput = int(input("Enter any number: "))
    loopKind(loopInput,intInput)
def loopKind(input,x):
    global time_start, time_end
    sum = 0
    i = 0
    match input:
        case 1:
            time_start = time.time()
            for i in range(x+1):
                sum+=i
                i+=1
            time_end = time.time()
            endCall(x,sum)
        case 2:
            time_start = time.time()
            while x+1 > i:
                sum+=i
                i+=1
            time_end = time.time()
            endCall(x,sum)
        case _:
            print("========== PLEASE ENTER THE PROPER INPUT ==========")
            start()
def endCall(x,sum):
    time_total = time_end - time_start
    print("The sum of all numbers from 1 to {} is {}." .format(x,sum))
    print("The time for the whole operation is {}" .format(time_total))

"========== CODE STARTS HERE =========="
start()

'''
DATA TABLE

n = 10
For loop time   = 0.0
While loop time = 0.0

n = 100
For loop time   = 0.0
While loop time = 0.0

n = 1,000
For loop time   = 0.0
While loop time = 0.0

n = 10,000
For loop time   = 0.0009808540344238281 
While loop time = 0.001009225845336914

n = 100,000
For loop time   = 0.006993293762207031
While loop time = 0.009038448333740234 

With the data above, it's safe to assume that using a for loop is faster

'''