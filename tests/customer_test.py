

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from customer import Customer

from customer import Customer

def test_customer_name_validation():
    c = Customer("Test")
    assert c.name == "Test"
