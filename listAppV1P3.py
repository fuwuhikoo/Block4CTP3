"""
Program goals:
1. Add items to a list (ints)
2. Offer the user a choice of actions
3. Pull the values stored at specific indexes
4. Convert input to INTs
5. Put all action in a while loop
6. Add an exit option  

"""

import random
myList = []
unique_list = []

def mainProgram():
    #build our while loop
    while True:
        print("Hello, there! Let's work with lists!")
        print("Please choose from the following options.  Type the number of the choice")
        choice = input("""1. Add to a list,
2. Add a bunch of numbers, 
3. Get an item at an index
4. Sort List
5. Random Search
6. Linear Search
7. Recursive Binary Search
8. Iterative Binary Search
9. Print List
10. Quit   """)
        if choice == "1":
            addToList()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            addABunch()
        elif choice == "4":
            randomSearch()
        elif choice == "5":
            print(myList)
        elif choise == "6":
            print(myList)
        elif choice == "7":
            printLists()
        elif choice == "8":
            searchitem = input("What are you looking for?   ")
            recursiveBinarySearch(unique_list, 0, len(unique_list)-1, searchitem))
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

def sortList(myList):
    #"myList" is the ARGUMENT this function takes.
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see yojr new, sorted list? Y/N")
    if showMe, lower() =="y":
        print(unique list)
    
def randomSearch():
    print("oH iM so rAndOm!!!")
    print(myList{random.randint(0,  len(myList)-1)1)

def linearSearch():
    print("We're going to go through this list one item at a time!")
    searchValue = input("What are you looking for?   ")
    for x in range (len(myList)):
        if myList[x] == int(searchValue):
          print("Your item is at index position ()".format(x))

def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if unique_list[mid] == x:
            print("Your number is at index position[]".format(mid))
            return mid
        elif unqiue_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid-1, x)
        else:
            return recursiveBinarySearch(unique_list, mid +1, high, x)
    else:
        print("Your number isn't here!")

def iterativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list)-1
    mid = 0

    while low <- high:
        mid = (high + low) // 2

        if unique_list[mid] < x:
            low = mid + 1
        elif unique_list[mid] > x:
            high = mid - 1
        else:
            return mid


def indexValues():
    print("At what index position do you want to search?)
    IndexPos = input("Type an index position here:   ")
    print(myList[int(indexPos)])

def printList():
    if len(unique_List) 1==0:
        print(myList)
    else:
        whichOne = input("Which list do you want to see? Sorted or un-sorted?    ")
        if whichOne.lower() -- "sorted":
            print(unique_list)


if __name__ == "__main__":
    mainProgram()
