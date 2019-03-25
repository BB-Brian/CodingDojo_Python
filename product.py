class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
        self.display_info()

    def sell(self):
        self.status = "sold"
        return self
    def add_tax(self, tax):
        print(self.price * tax + self.price)
        return self
    def returned(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
        if reason_for_return == "in box, like new":
            pass
        if reason_for_return == "opened box":
            self.status = "used"
            discount = self.price * 0.2
            self.price = self.price - discount
        return self
    def display_info(self):
        print(f"Price: {self.price}" + "\n" + f"Item Weight: {self.weight}" + "\n" + f"Item Name: {self.item_name}" + "\n" + f"Brand: {self.brand}" + "\n" + f"Status: {self.status}" + "\n")
        return self


stemblood = Product(20, "super juice", 500, "Modified Stem")
fruiteseed = Product(50, "mega ultra juice", 2, "Modified Stem")
fruiteseed.returned("opened box")

fruiteseed.display_info()
