from .store import *
from .ingredients import *

def test_ny_pizza():
    store = NYPizzaStore()
    pizza1 = store.order_pizza("cheese")
    assert pizza1.name == "NY Style Cheese Pizza"
    assert pizza1.dough.name == "Thin Crust Dough"
    assert pizza1.sauce.name == "Marinara Sauce"
    assert pizza1.cheese.name == "Reggiano Cheese"
