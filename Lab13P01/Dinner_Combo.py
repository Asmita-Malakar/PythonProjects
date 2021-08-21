class Dinner_combo:

    def __init__(self):
        self._main_dish = ''
        self._soup = ''
        self._total = 0
    def choose_dish(self):
        dishInput = input(('Enter 1 for sweet and sour pork [$7], 2 for sesame chicken [$8] '
                           'or 3 for shrimp fired rice [$9]: '))
        amount = 0
        if dishInput == '1':
            self._main_dish = 'sweet and sour pork'
            amount = amount + 7
        elif dishInput == '2':
            self._main_dish = 'sesame chicken'
            amount = amount + 8
        elif dishInput == '3':
            self._main_dish = 'shrimp fried rice'
            amount = amount + 9
        return self._main_dish, amount

    def choose_soup(self):
        soupInput = input("Enter 1 for egg drop soup [$1.25] or 2 for wanton soup [$1.50]: ")
        amount = 0
        if soupInput == '1':
            self._soup = 'egg drop'
            amount = amount + 1.25
        elif soupInput == '2':
            self._soup = 'wanton'
            amount = amount + 1.50
        return self._soup, amount

    def displayOrder(self):
        mainDish = list(self.choose_dish())
        soup = list(self.choose_soup())
        self._total = mainDish[1] + soup[1]
        return (f"Items ordered: {mainDish}, {soup}\n" + f"Please pay this amount: {self._total}")

        pass




