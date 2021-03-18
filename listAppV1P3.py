"""
Program goals:
1. Add items to a list (ints)
2. Offer the user a choice of actions
3. Pull the values stored at specific indexes
4. Convert input to INTs
5. Put all action in a while loop
6. Add an exit option  

"""

def mainProgram():
    #build our while loop
    while True
        myList = []
        print("Hello, there! Let's work with lists!")
        print("Please choose from the following options.  Type the number of the choice")
        choice = input("1. Add to a list,
2. Return a value at a list
3. Random Search
4. Print List 
5. Quit   ""
        if choice == "1":
            addToList()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            addABunch()
        elif choice == "4":
            randomSearch()
        elif choice == "5"
            print(myList)
        else:
            break

def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!  ")
    myList.append(int(newItem))
    #we need to think about errors!


def addABunch():
    print("We're gonna add a bunch of numbers to your list!")
    numToAdd = input("How many new intergers would you like to add?   ")
    numRange = input("And how high would you like these number to go?   ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is completed !")
    
def randomSearch():
    print("oH iM so rAndOm!!!")
    print(myList{random.randint(0,  len(myList
    

def indexValues():
    print("At what index position do you want to search?)
    IndexPos = input("Type an index position here:   ")
    print(myList[int(indexPos)]) 


if __name__ == "__main__":
    mainProgram()
