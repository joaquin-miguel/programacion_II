from abc import ABC, abstractmethod

class Pizza(ABC):
    name: str = "Generic Pizza"
    toppings: list[str] = []

    def prepare(self):
        print(f"Preparing {self.name}")
        print("Adding toppings:", ", ".join(self.toppings))

    def bake(self): print("Bake 25 min at 350")
    def cut(self):  print("Cutting pizza into diagonal slices")
    def box(self):  print("Place pizza in official box")
    def __str__(self): return self.name

class NYStyleCheesePizza(Pizza):
    def __init__(self):
        self.name="NY Style Sauce & Cheese"; 
        self.toppings=["Reggiano cheese"]

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        self.name="Chicago Style Deep Dish Cheese"; 
        self.toppings=["Shredded Mozzarella"]
    def cut(self): print("Cutting the pizza into square slices")

# Se agregan las nuevas variantes de pizzas

# Veggie Pizzas
class NYStyleVeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Veggie Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings = ["Grated Reggiano Cheese", "Garlic", "Onion", "Mushrooms", "Red Pepper"]

class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Veggie Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings = ["Shredded Mozzarella Cheese", "Black Olives", "Spinach", "Eggplant"]

    def cut(self):
        # Chicago suele cortar en cuadrados
        print("Cutting the pizza into square slices")

# Pepperoni Pizzas
class NYStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Pepperoni Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings = ["Grated Reggiano Cheese", "Sliced Pepperoni", "Garlic", "Onion", "Mushrooms", "Red Pepper"]


class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Pepperoni Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings = ["Shredded Mozzarella Cheese", "Sliced Pepperoni", "Black Olives", "Spinach", "Eggplant"]

    def cut(self):
        print("Cutting the pizza into square slices")
