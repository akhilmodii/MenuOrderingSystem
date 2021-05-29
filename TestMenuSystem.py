import unittest
from Src import MenuSystem


class TestMenuSystem(unittest.TestCase):
    # Instantiating the object to be tested
    menu = MenuSystem.Menu()
    menu.addToBreakfast('1', 'Eggs')
    menu.addToBreakfast('2', 'Toast')
    menu.addToBreakfast('3', 'Coffee')

    menu.addToLunch('1', 'Sandwich')
    menu.addToLunch('2', 'Chips')
    menu.addToLunch('3', 'Soda')

    menu.addToDinner('1', 'Steak')
    menu.addToDinner('2', 'Potatoes')
    menu.addToDinner('3', 'Wine')
    menu.addToDinner('4', 'Cake')

    # Testing all the functionalities for Breakfast
    def test_addToBreakfast(self):
        self.assertEqual(TestMenuSystem.menu.breakfastMenu, {'1': 'Eggs', '2': 'Toast', '3': 'Coffee'},
                         'Should return correct dict for breakfast')

    def test_getBreakfastList_Normal(self):
        idList = ['1', '2', '3']
        self.assertEqual(TestMenuSystem.menu.getBreakfastList(idList), ['Eggs', 'Toast', 'Coffee'],
                         'Should return a list with Eggs, Toast, and Coffee')

    def test_getBreakfastList_NoDrink(self):
        idList = ['1', '2']
        self.assertEqual(TestMenuSystem.menu.getBreakfastList(idList), ['Eggs', 'Toast', 'Water'],
                         'Should return a list with Eggs, Toast, and Water')

    def test_getBreakfastList_MultipleCoffee(self):
        idList = ['1', '2', '3', '3', '3', '3']
        self.assertEqual(TestMenuSystem.menu.getBreakfastList(idList), ['Eggs', 'Toast', 'Coffee(4)'],
                         'Should return a list with Eggs, Toast, and fours cups Coffee')

    def test_getBreakfastList_SideMissing(self):
        idList = ['1', '3']
        self.assertEqual(TestMenuSystem.menu.getBreakfastList(idList), [], 'Should not take the order')

    def test_getBreakfastList_MainMissing(self):
        idList = ['2', '3']
        self.assertEqual(TestMenuSystem.menu.getBreakfastList(idList), [], 'Should not take the order')

    def test_getBreakfastList_CorrectOrder(self):
        idList = ['3', '1', '2']
        self.assertEqual(TestMenuSystem.menu.getBreakfastList(idList), ['Eggs', 'Toast', 'Coffee'],
                         'Should return a list with Eggs, Toast, and Coffee in the same order')

    # Testing all the functionalities for Lunch
    def test_addtoLunch(self):
        self.assertEqual(TestMenuSystem.menu.lunchMenu, {'1': 'Sandwich', '2': 'Chips', '3': 'Soda'},
                         'Should return correct dict for lunch')

    def test_getLunchList_Normal(self):
        idList = ['1', '2', '3']
        self.assertEqual(TestMenuSystem.menu.getLunchList(idList), ['Sandwich', 'Chips', 'Soda'],
                         'Should return a list with Sandwich, Chips, and Soda')

    def test_getLunchList_NoDrink(self):
        idList = ['1', '2']
        self.assertEqual(TestMenuSystem.menu.getLunchList(idList), ['Sandwich', 'Chips', 'Water'],
                         'Should return a list with Sandwich, Chips, and Water')

    def test_getLunchList_MultipleChips(self):
        idList = ['1', '2', '2', '2', '3']
        self.assertEqual(TestMenuSystem.menu.getLunchList(idList), ['Sandwich', 'Chips(3)', 'Soda'],
                         'Should return a list with Eggs, four Chips, and Soda')

    def test_getLunchList_SideMissing(self):
        idList = ['1', '3']
        self.assertEqual(TestMenuSystem.menu.getLunchList(idList), [], 'Should not take the order')

    def test_getLunchList_MainMissing(self):
        idList = ['2', '3']
        self.assertEqual(TestMenuSystem.menu.getLunchList(idList), [], 'Should not take the order')

    def test_getLunchList_CorrectOrder(self):
        idList = ['2', '3', '1']
        self.assertEqual(TestMenuSystem.menu.getLunchList(idList), ['Sandwich', 'Chips', 'Soda'],
                         'Should return a list with Sandwich, Chips, and Soda in the same order')

    # Testing all the functionalities for Dinner
    def test_addtoDinner(self):
        self.assertEqual(TestMenuSystem.menu.dinnerMenu, {'1': 'Steak', '2': 'Potatoes', '3': 'Wine', '4': 'Cake'},
                         'Should return correct dict for dinner')

    def test_getDinnerList_Normal(self):
        idList = ['1', '2', '3', '4']
        self.assertEqual(TestMenuSystem.menu.getDinnerList(idList), ['Steak', 'Potatoes', 'Wine', 'Water', 'Cake'],
                         'Should return a list with Steak, Potatoes, Wine, Water, and Cake')

    def test_getDinnerList_NoDrink(self):
        idList = ['1', '2', '4']
        self.assertEqual(TestMenuSystem.menu.getDinnerList(idList), ['Steak', 'Potatoes', 'Water', 'Cake'],
                         'Should return a list with Steak, Potaotes, Water, and Cake')

    def test_getDinnerList_DessertMissing(self):
        idList = ['1', '2', '3']
        self.assertEqual(TestMenuSystem.menu.getDinnerList(idList), [], 'Should not take the order')

    def test_getDinnerList_SideMissing(self):
        idList = ['1', '3', '4']
        self.assertEqual(TestMenuSystem.menu.getDinnerList(idList), [], 'Should not take the order')

    def test_getDinnerList_MainMissing(self):
        idList = ['2', '3', '4']
        self.assertEqual(TestMenuSystem.menu.getDinnerList(idList), [], 'Should not take the order')

    def test_getDinnerList_CorrectOrder(self):
        idList = ['1', '3', '4', '2']
        self.assertEqual(TestMenuSystem.menu.getDinnerList(idList), ['Steak', 'Potatoes', 'Wine', 'Water', 'Cake'],
                         'Should return a list with Steak, Potatoes, Wine, Water, and Cake in the same order')
