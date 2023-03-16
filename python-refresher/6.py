class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        self.items.append({"name": name, "price": price})

    def stock_price(self):
        rslt = 0
        for item in self.items:
            rslt += item["price"]
        return rslt
