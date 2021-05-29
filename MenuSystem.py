# Defining a class Menu
class Menu:
    # Dictionaries to store the menu for each meal
    breakfastMenu = {}
    lunchMenu = {}
    dinnerMenu = {}

    def __init__(self):
        pass

    # Populate the Breakfast Dictionary
    def addToBreakfast(self, id, name):
        Menu.breakfastMenu[id] = name

    # Returning the order for Breakfast if all the rules are matched
    def getBreakfastList(self, idList):
        mainList = []
        sideList = []
        drinkList = []

        if checkMissing(idList):  # Checking for missing main or side
            return []

        for i in idList:
            if i == '1':
                mainList.append(Menu.breakfastMenu[i])
            elif i == '2':
                sideList.append(Menu.breakfastMenu[i])
            elif i == '3':
                drinkList.append(Menu.breakfastMenu[i])
        if '3' not in idList:  # Checking if drink is missing
            drinkList.append('Water')

        # Counting multiple orders for side or drink
        numberOfSides = sideList.count('Toast')
        numberOfDrinks = drinkList.count('Coffee')

        if numberOfSides > 1:
            sideList = list(set(sideList))
            string = sideList[0] + '(' + str(numberOfSides) + ')'
            sideList.clear()
            sideList.append(string)

        if numberOfDrinks > 1:
            drinkList = list(set(drinkList))
            string = drinkList[0] + '(' + str(numberOfDrinks) + ')'
            drinkList.clear()
            drinkList.append(string)

        # The final list for the order
        breakfastList = mainList + sideList + drinkList
        return breakfastList

        # Populate the Lunch Dictionary

    def addToLunch(self, id, name):
        Menu.lunchMenu[id] = name

    # Returning the order for Lunch if all the rules are matched
    def getLunchList(self, idList):
        mainList = []
        sideList = []
        drinkList = []

        if checkMissing(idList):
            return []

        if idList.count('1') > 1:  # Checking for multiple orders of Sandwich
            print('Unable to process: Sandwich cannot be ordered more than once')
            return []

        for i in idList:
            if i == '1':
                mainList.append(Menu.lunchMenu[i])
            elif i == '2':
                sideList.append(Menu.lunchMenu[i])
            elif i == '3':
                drinkList.append(Menu.lunchMenu[i])
        if '3' not in idList:
            drinkList.append('Water')

        numberOfSides = sideList.count('Chips')
        numberOfDrinks = drinkList.count('Soda')

        if numberOfSides > 1:
            sideList = list(set(sideList))
            string = sideList[0] + '(' + str(numberOfSides) + ')'
            sideList.clear()
            sideList.append(string)

        if numberOfDrinks > 1:
            drinkList = list(set(drinkList))
            string = drinkList[0] + '(' + str(numberOfDrinks) + ')'
            drinkList.clear()
            drinkList.append(string)

        # The final list
        lunchList = mainList + sideList + drinkList
        return lunchList

    # Populating the Dinner Dictionary
    def addToDinner(self, id, name):
        Menu.dinnerMenu[id] = name

    # Returning the order for Dinner if all the rules are matched
    def getDinnerList(self, idList):
        mainList = []
        sideList = []
        drinkList = []
        dessertList = []

        if checkMissing(idList):
            return []

        if idList.count('1') > 1:  # Checking for multiple orders of Steak
            print('Unable to process: Steak cannot be ordered more than once')
            return []

        if checkDessert(idList):
            return []

        for i in idList:
            if i == '1':
                mainList.append(Menu.dinnerMenu[i])
            elif i == '2':
                sideList.append(Menu.dinnerMenu[i])
            elif i == '3':
                drinkList.append(Menu.dinnerMenu[i])
            elif i == '4':
                dessertList.append(Menu.dinnerMenu[i])
        drinkList.append('Water')

        numberOfSides = sideList.count('Potatoes')
        numberOfDrinks = drinkList.count('Wine')

        if numberOfSides > 1:
            sideList = list(set(sideList))
            string = sideList[0] + '(' + str(numberOfSides) + ')'
            sideList.clear()
            sideList.append(string)

        if numberOfDrinks > 1:
            drinkList = list(set(drinkList))
            string = drinkList[0] + '(' + str(numberOfDrinks) + ')'
            drinkList.clear()
            drinkList.append(string)

        # The final list
        dinnerList = mainList + sideList + drinkList + dessertList
        return dinnerList


# Method to check if the main or side is missing from the order
def checkMissing(idList):
    if '1' not in idList:
        print('Unable to process: Main is missing')
        return True
    elif '2' not in idList:
        print('Unable to process: Side is missing')
        return True
    else:
        return False


# Method to check if the dessert is missing from the dinner order
def checkDessert(idList):
    if '4' not in idList:
        print('Unable to process: Dessert is missing')
        return True
    return False


if __name__ == '__main__':
    print('Enter what would you like to order.\n')
    print('Enter exit to quit.\n')
    while True:
        inp = input('Input: ')  # Taking input
        try:
            lst = inp.split(' ')
            itemIdList = lst[1].split(',')

            if lst[0] == 'exit':
                print('Good Bye')
                break

            menu = Menu()  # Instantiating the Menu object
            # Breakfast Menu
            menu.addToBreakfast('1', 'Eggs')
            menu.addToBreakfast('2', 'Toast')
            menu.addToBreakfast('3', 'Coffee')
            # Lunch Menu
            menu.addToLunch('1', 'Sandwich')
            menu.addToLunch('2', 'Chips')
            menu.addToLunch('3', 'Soda')
            # Dinner Menu
            menu.addToDinner('1', 'Steak')
            menu.addToDinner('2', 'Potatoes')
            menu.addToDinner('3', 'Wine')
            menu.addToDinner('4', 'Cake')

            if lst[0] == 'Breakfast' or lst[0] == "breakfast":  # Order for Breakfast
                output = ', '.join(menu.getBreakfastList(itemIdList))
                print(output)

            elif lst[0] == 'Lunch' or lst[0] == 'lunch':  # Order for Lunch
                output = ', '.join(menu.getLunchList(itemIdList))
                print(output)

            elif lst[0] == 'Dinner' or lst[0] == 'dinner':  # Order for Dinner
                output = ', '.join(menu.getDinnerList(itemIdList))
                print(output)

        except IndexError:  # Catching the exception
            if lst[0] == 'exit':
                print('Good Bye')
                break
            else:
                print('Unable to process: Main is missing, Side is missing')
