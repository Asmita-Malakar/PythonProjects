from Dinner_Combo import Dinner_combo


class Deluxe_dinner_combo(Dinner_combo):

    def __init__(self):
        super().__init__()
        self._appetizer = ''
    def choose_appetizer(self):
        appetizerInput = input("Enter 1 for egg drop soup [$1.25] or 2 for wanton soup [$1.50]: ")
        amount = 0
        if appetizerInput == '1':
            self._appetizer = 'spring roll'
            amount = amount + 1.25
        elif appetizerInput == '2':
            self._appetizer = 'chicken wing'
            amount = amount + 1.50
        return self._appetizer, amount

    def displayOrder(self):
        mainDish = list(self.choose_dish())
        soup = list(self.choose_soup())
        appetizer = list(self.choose_appetizer())
        self._total = mainDish[1] + soup[1] + appetizer[1]
        message = f"Items ordered: {mainDish[1]}, {soup[1]}, {appetizer[1]}\n Please pay this amount: {self._total}"
        return message



