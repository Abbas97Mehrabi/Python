import csv

class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float,  quantity: 0):
        assert price >= 0, f"Price {price} is not greater or equal than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal than zero!"

        self.__name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)
    @property
    def price(self):
        return self.__price
    

    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @classmethod
    def instantiate_from_csv(cls):
        with open('PythonTutorial/ObjectOrientatedProgramming/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, float):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"
    
class Phone(Item):
    def __init__(self, name: str, price: float,  quantity: 0, broken_phones=0):
        super().__init__(name, price, quantity)

        assert broken_phones >= 0, f"Price {broken_phones} is not greater or equal than zero!"

        self.broken_phones = broken_phones

        

phone1 = Phone(name="iphone 7", price=400, quantity=2,broken_phones=1)
phone1.apply_increment(0.2)
print(phone1.price)
#print(item2.__dict__)
        