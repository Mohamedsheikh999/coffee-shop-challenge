from customer import Customer
from coffee import Coffee

c1 = Customer("Alice")
c2 = Customer("Bob")

coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")

c1.create_order(coffee1, 3.5)
c1.create_order(coffee2, 4.0)
c2.create_order(coffee1, 5.0)

print(coffee1.customers())  # [Alice, Bob]
print(c1.coffees())         # [Espresso, Latte]
print(coffee1.num_orders()) # 2
print(coffee1.average_price())  # 4.25
print(Customer.most_aficionado(coffee1).name)  # Bob
