class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string with 1–15 characters.")

    def orders(self):
        return self._orders

    def coffees(self):
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        from order import Order
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        customer_spend = {}
        for order in coffee.orders():
            customer_spend[order.customer] = customer_spend.get(order.customer, 0) + order.price
        if not customer_spend:
            return None
        return max(customer_spend, key=customer_spend.get)
