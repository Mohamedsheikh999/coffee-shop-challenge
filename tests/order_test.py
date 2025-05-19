
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from customer import Customer



from customer import Customer
from coffee import Coffee
from order import Order

def test_order_creation():
    c = Customer("Test")
    coffee = Coffee("Americano")
    o = Order(c, coffee, 5.0)
    assert o.customer == c
    assert o.coffee == coffee
    assert o.price == 5.0
