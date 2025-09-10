from abc import ABC, abstractmethod
from .ingredients import PizzaIngredientFactory

class Pizza(ABC):
    def __init__(self, name: str, ing_factory: PizzaIngredientFactory):
        self.name=name; self.f=ing_factory
        self.dough=None; self.sauce=None; self.cheese=None; self.clam=None
    @abstractmethod
    def prepare(self): ...
    def bake(self): print("Bake 25 min at 350")
    def cut(self):  print("Cutting pizza into diagonal slices")
    def box(self):  print("Place pizza in official box")
    def __str__(self): return self.name

class CheesePizza(Pizza):
    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough=self.f.create_dough(); 
        self.sauce=self.f.create_sauce(); 
        self.cheese=self.f.create_cheese()
        print(" ->", self.dough, "/", self.sauce, "/", self.cheese)

class ClamPizza(Pizza):
    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough=self.f.create_dough(); 
        self.sauce=self.f.create_sauce(); 
        self.cheese=self.f.create_cheese(); 
        self.clam=self.f.create_clam()
        print(" ->", self.dough, "/", self.sauce, "/", self.cheese, "/", self.clam)

# Se crean las clases `VeggiePizza` y `PepperoniPizza`.
class VeggiePizza(Pizza):
    def __init__(self, name: str, ingredient_factory):
        super().__init__(name, ingredient_factory)

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()
        print(" ->", self.dough, "/", self.sauce, "/", self.cheese, "/", self.veggies)  

class PepperoniPizza(Pizza):
    def __init__(self, name: str, ingredient_factory):
        super().__init__(name, ingredient_factory)

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.pepperoni = self.ingredient_factory.create_pepperoni()
        print(" ->", self.dough, "/", self.sauce, "/", self.cheese, "/", self.pepperoni)
