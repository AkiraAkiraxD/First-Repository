userList = ["12207163","12214450","11764209","11956166","16170505"]
passList = ["lboec2abcde","FrtntChgJgWthY","NvrGnnGvYUp","SnSnCtyWsntMdFrY","NnNknQntssntlQntplts"]


def usernameCheck(usrnm,psswrd):
    i=0
    try:
        while i <= len(userList):
            if userList[i] != usrnm:
                i+=1
            else:
                if passList[i] != psswrd:
                    i+=1
                else:
                    print("Access Granted!")
                    break
        if i > len(userList):
            print("username or password is incorrect!")
    except IndexError:
        print("username or password is incorrect!")

#========== PROGRAM STARTS HERE ==========
inputUsername = str(input("Enter Username: "))
inputPassword = str(input("Enter Password: "))
usernameCheck(inputUsername,inputPassword)