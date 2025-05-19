

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from customer import Customer

from coffee import Coffee

def test_coffee_name():
    coffee = Coffee("Mocha")
    assert coffee.name == "Mocha"
