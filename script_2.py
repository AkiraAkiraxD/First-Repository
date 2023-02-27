import script_1
import script_1

def fix(x):
    global finalInput, finalValue
    temp = x.casefold()
    temp = temp.replace(" ","")
    checkValue()
    finalInput = temp
    checkUnit(finalInput[count-1:])
def checkValue():
    global finalValue
    try:
        finalValue = int(inputTemperature[:count-1])
    except ValueError:
        print("Error: Value contains multiple letters.")
        quit()
def checkUnit(letter):
    global unitMeasurement
    match letter:
        case "c":
            unitMeasurement = "celsius"
            displayChoices(unitMeasurement)
        case "f":
            unitMeasurement = "fahrenheit"
            displayChoices(unitMeasurement)
        case "k":
            unitMeasurement = "kelvin"
            displayChoices(unitMeasurement)
        case _:
            print("Error: Invalid Unit")
def displayChoices(unit):
    global action
    match unit:
        case "celsius":
            action = int(input("/ 1=Convert to Fahrenheit / 2=Convert to Kelvin /: "))
            computation(unit,action)
        case "fahrenheit":
            action = int(input("/ 1=Convert to Celsius / 2=Convert to Kelvin /: "))
            computation(unit,action)
        case "kelvin":
            action = int(input("/ 1=Convert to Celsius / 2=Convert to Fahrenheit /: "))
            computation(unit,action)
        case _:
            print("Error: Invalid Input")
            displayChoices(unitMeasurement)
def computation(unit,choice):
    global ans
    ans = 0
    finalValue = int(inputTemperature[:count-1])
    temporary = finalValue
    match unit:
        case "celsius":
            if choice == 1:
                script_1.fahrenheit(finalValue)
                print("{}C is {}F" .format(temporary,script_1.ans))
            else:
                script_1.kelvin(finalValue)
                print("{}C is {}K" .format(temporary,script_1.ans))
        case "fahrenheit":
            if choice == 1:
                script_1.celsius(finalValue)
                print("{}F is {}C" .format(temporary,script_1.ans))
            else:
                script_1.celsius(finalValue)
                script_1.kelvin(script_1.ans)
                print("{}F is {}K" .format(temporary,script_1.ans))
        case "kelvin":
            if choice == 1:
                script_1.k2c(finalValue)
                print("{}K is {}C" .format(temporary,script_1.ans))
            else:
                script_1.k2c(finalValue)
                script_1.fahrenheit(script_1.ans)
                print("{}K is {}F" .format(temporary,script_1.ans))

#========== Code Starts Here ==========
inputTemperature = str(input("Input Temperature: "))
count = len(inputTemperature)

fix(inputTemperature)