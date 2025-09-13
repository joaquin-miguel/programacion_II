from abc import ABC, abstractmethod

# Ingredient products
class Dough:    
    def __init__(self, name): 
        self.name=name;
      
    def __str__(self): 
        return self.name

class Sauce:    
    def __init__(self, name): 
        self.name=name; 
     
    def __str__(self): 
        return self.name

class Cheese:   
    def __init__(self, name): 
        self.name=name;  
    def __str__(self): 
        return self.name
    
class Clams:    
    def __init__(self, name): 
        self.name=name;  
    def __str__(self): 
        return self.name
"""    
# Se agregan dos nuevos ingredientes abstractos
class Veggies(ABC):
    @abstractmethod
    def __str__(self) -> str: ...

class Pepperoni(ABC):
    @abstractmethod
    def __str__(self) -> str: ...
"""
class Veggies(ABC):
    def __str__(self):
        return self.__class__.__name__
    def __repr__(self):
        return str(self)

class Pepperoni(ABC):
    def __str__(self):
        return self.__class__.__name__
    def __repr__(self):
        return str(self)    
    
# Se agregan clasen concretas de Veggies

class Onion(Veggies):
    def __str__(self): 
        return "Onion"

class Mushroom(Veggies):
    def __str__(self): 
        return "Mushroom"

class Garlic(Veggies):
    def __str__(self): 
        return "Garlic"

class Spinach(Veggies):
    def __str__(self): 
        return "Spinach"

class BlackOlives(Veggies):
    def __str__(self): 
        return "Black Olives"

class RedPepper(Veggies):
    def __str__(self): 
        return "Red Pepper"

# Se agrega clase concreta de Pepperoni

class SlicedPepperoni(Pepperoni):
    def __str__(self): 
        return "Sliced Pepperoni"

# Abstract Factory
class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self) -> Dough: ...
    @abstractmethod
    def create_sauce(self) -> Sauce: ...
    @abstractmethod
    def create_cheese(self) -> Cheese: ...
    @abstractmethod
    def create_clam(self) -> Clams: ...
    # Se agregan los Nuevos métodos
    @abstractmethod
    def create_veggies(self) -> list: ...
    @abstractmethod
    def create_pepperoni(self): ...

# Concrete factories
class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:  
        return Dough("Thin Crust Dough")
    def create_sauce(self) -> Sauce:  
        return Sauce("Marinara Sauce")
    def create_cheese(self) -> Cheese:
        return Cheese("Reggiano Cheese")
    def create_clam(self) -> Clams:   
        return Clams("Fresh Clams")
    # Se agregan los Nuevos métodos
    def create_veggies(self):
        return [Garlic(), Onion(), Mushroom(), RedPepper()]
    def create_pepperoni(self):
        return SlicedPepperoni()

class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:  
        return Dough("Thick Crust Dough")
    def create_sauce(self) -> Sauce:  
        return Sauce("Plum Tomato Sauce")
    def create_cheese(self) -> Cheese:
        return Cheese("Mozzarella Cheese")
    def create_clam(self) -> Clams:   
        return Clams("Frozen Clams")
    # Se agregan los Nuevos métodos
    def create_veggies(self):
        return [BlackOlives(), Spinach(), RedPepper()]

    def create_pepperoni(self):
        return SlicedPepperoni()
