class Water_bill:
    def __init__(self,name, address):
        self.name = name
        self.address = address
        self.total = 0
        self.gallons = (0)

    def calculate_charge(self):
        self.gallons = input("How many gallons of water were used? ")
        if self.gallons <= str(6000):
            self.total = self.gallons * int(0.005)
        elif self.gallons > str(6000):
            self.total = ((int(self.gallons) - 6000) * 0.007) + 30
        return self.gallons

    def display_bill(self):
        return f"Name: {self.name}\n Address: {self.address}\n Gallons used: {self.gallons}\n Please pay this amount" \
               f": {self.total}"
