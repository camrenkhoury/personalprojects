#welcome message
#ask for users input for number of characters
#take three symbols from an array storage
#pick two random capital letters from a capitalcase letter storage
#Pick two random lowercase letters from a lowercase letter storage
#put eight characters into a a set
#compare length of set to input number of characters
#randomly insert lowercase and capital letters until length matchs
#take set and randomize the characters
#print array as string
#repeat ten times
#ask the user if it wants regeneration of passwords (10 more with same number of characters)
#restart program


def restart():  
    import math
    import random

    symbolArray = ["!","@","#","$","%","^","&","*","(",")","-","=","+","_","{","}","[","]"]
    capitalArray = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z",
                    "X","C","V","B","N","M"]
    lowerArray = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z",
                  "x","c","v","b","n","m"]

    characterStorage = []


    #character array library 

    print("Welcome to Random Password Generator!")

    #welcome statement ^

    def dataCollection(): #defines data collection function
            
        try:
            global lengthPassword
            lengthPassword = int(input("Enter your desired password length for ten secure password combinations \n"))

            if lengthPassword < 8 or lengthPassword > 32:
                print("Make sure you are using an integer number between 8-32")
                dataCollection()

            #checks password range
                
            elif lengthPassword >= 8 and lengthPassword <= 32:
                print("You have requested", lengthPassword,"characters in your password")
            
        except ValueError:
            print("Make sure you are using an integer number between 8-32")
            dataCollection()

        #^makes sure negatives and decimals are not used


    dataCollection() #calls data collection function

    def passwordGeneration(size): #password generation function

    #symbol generation

        while len(characterStorage) < 3:
            number = random.randint(0,17)
            if symbolArray[number] in characterStorage:
                characterStorage.append(symbolArray[random.randint(0,17)])
            else:
                characterStorage.append(symbolArray[number])

                #^ gives 3 random symbols

        while len(characterStorage) >= 3 and len(characterStorage) < 5:
            number = random.randint(0,25)
            if capitalArray[number] in characterStorage:
                characterStorage.append(capitalArray[random.randint(0,25)])
            else:
                characterStorage.append(capitalArray[number])

                #^ gives 3 random capital letters

        while len(characterStorage) >= 5 and len(characterStorage) <7:
            number = random.randint(0,25)
            if lowerArray[number] in characterStorage:
                characterStorage.append(lowerArray[random.randint(0,25)])
            else:
                characterStorage.append(lowerArray[number])

            #^ gives 3 random lowercase letters

        characterStorage.append(str(random.randint(0,9)))

            #^ adds random number for minimum 8 characters



        def fillPassword(): 
            while len(characterStorage) < size:
                decision = random.randint(1,3)

                if decision == 1:
                    number = random.randint(0,25)
                    if lowerArray[number] in characterStorage:
                        characterStorage.append(lowerArray[random.randint(0,25)]) #adds additional lower case letter
                    else:
                        characterStorage.append(lowerArray[number])  #decreases chance of repeat

                elif decision == 2:
                    number = random.randint(0,25) 
                    if capitalArray[number] in characterStorage: 
                        characterStorage.append(capitalArray[random.randint(0,25)]) #adds additional random capital letter
                    else:
                        characterStorage.append(capitalArray[number])  #decreases chance of repeat 

                elif decision == 3:
                    characterStorage.append(str(random.randint(0,9)))  #adds random number
                    


            #^ generates random characters for rest of password (not symbols)

        fillPassword()                    
        random.shuffle(characterStorage)
        password = ''.join([str(item) for item in characterStorage])
        print(password)

        while len(characterStorage) > 0:
            characterStorage.pop(0)


    print("Ten Passwords presented below")

    k = 0
    while k < 10:
        k  =  k  + 1
        
        passwordGeneration(lengthPassword)

    restart()
    
restart()
