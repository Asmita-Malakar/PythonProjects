class Electricity_bill:
    def __init__(self,name, address):
        self.name = name
        self.address = address
        self.total = 0
        self.kilowatts = (0)

    def calculate_charge(self):
        self.kilowatts = input("How many gallons of water were used? ")
        if self.kilowatts <= str(500):
            self.total = self.kilowatts * int(0.12)
        elif self.kilowatts > str(6000):
            self.total = ((int(self.kilowatts) - 500) * 0.15) + 60
        return self.kilowatts

    def display_bill(self):
        return f"Name: {self.name}\n Address: {self.address}\n Gallons used: {self.kilowatts}\n Please pay" \
               f" this amount: {self.total}"
