from .store import *
from .ingredients import *

def test_ny_pizza():
    store = NYPizzaStore()
    pizza1 = store.order_pizza("cheese")
    pizza2 = store.order_pizza("clam")
    pizza3 = store.order_pizza("veggie")
    pizza4 = store.order_pizza("pepperoni")
    assert pizza1.name == "NY Style Cheese Pizza"
    assert pizza2.name == "NY Style Clam Pizza"
    assert pizza3.name == "NY Style Veggie Pizza"
    assert pizza4.name == "NY Style Pepperoni Pizza"
    assert pizza1.dough.name == pizza2.dough.name == pizza3.dough.name == pizza4.dough.name == "Thin Crust Dough"
    assert pizza1.sauce.name ==  pizza2.sauce.name == pizza3.sauce.name == pizza4.sauce.name =="Marinara Sauce"
    assert pizza1.cheese.name == pizza2.cheese.name == pizza3.cheese.name == pizza4.cheese.name == "Reggiano Cheese"
    assert pizza2.clam.name == "Fresh Clams"
    assert len(pizza3.veggies) == 4
    assert isinstance(pizza3.veggies[0], Garlic)
    assert isinstance(pizza3.veggies[1], Onion)
    assert isinstance(pizza3.veggies[2], Mushroom)
    assert isinstance(pizza3.veggies[3], RedPepper)
    assert isinstance(pizza4.pepperoni, SlicedPepperoni)

def test_chi_pizza():
    store = ChicagoPizzaStore()
    pizza1 = store.order_pizza("cheese")
    pizza2 = store.order_pizza("clam")
    pizza3 = store.order_pizza("veggie")
    pizza4 = store.order_pizza("pepperoni")
    assert pizza1.name == "Chicago Style Cheese Pizza"
    assert pizza2.name == "Chicago Style Clam Pizza"
    assert pizza3.name == "Chicago Style Veggie Pizza"
    assert pizza4.name == "Chicago Style Pepperoni Pizza"
    assert pizza1.dough.name == pizza2.dough.name == pizza3.dough.name == pizza4.dough.name == "Thick Crust Dough"
    assert pizza1.sauce.name ==  pizza2.sauce.name == pizza3.sauce.name == pizza4.sauce.name =="Plum Tomato Sauce"
    assert pizza1.cheese.name == pizza2.cheese.name == pizza3.cheese.name == pizza4.cheese.name == "Mozzarella Cheese"
    assert pizza2.clam.name == "Frozen Clams"
    assert len(pizza3.veggies) == 3
    assert isinstance(pizza3.veggies[0], BlackOlives)
    assert isinstance(pizza3.veggies[1], Spinach)
    assert isinstance(pizza3.veggies[2], RedPepper)
    assert isinstance(pizza4.pepperoni, SlicedPepperoni)
