# condiments.py
# Contiene el Decorador Abstracto y los Decoradores Concretos.

from abc import ABC, abstractmethod
from beverages import Beverage

# --- Decorador Abstracto ---
class CondimentDecorator(Beverage, ABC):
    """
    Clase base para los decoradores de condimentos.
    Hereda de Beverage para tener el mismo tipo.
    Mantiene una referencia a la bebida que está envolviendo.
    """
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    def get_size(self):
        return self._beverage.get_size()

    @abstractmethod
    def get_description(self) -> str:
        pass

# --- Decoradores Concretos ---
class Milk(CondimentDecorator):
    """
    Decorador para añadir Leche a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Leche"

    def cost(self) -> float:
        size = self.get_size()
        if size == Beverage.TALL:
            extra = 0.10
        elif size == Beverage.GRANDE:
            extra = 0.15
        else:  # VENTI
            extra = 0.20
        return self._beverage.cost() + extra

class Mocha(CondimentDecorator):
    """
    Decorador para añadir Mocha a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Mocha"

    def cost(self) -> float:
        size = self.get_size()
        if size == Beverage.TALL:
            extra = 0.20
        elif size == Beverage.GRANDE:
            extra = 0.25
        else:  # VENTI
            extra = 0.30
        return self._beverage.cost() + extra

class Soy(CondimentDecorator):
    """
    Decorador para añadir Soja a una bebida.
    """

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Soja"

    def cost(self) -> float:
        size = self.get_size()
        if size == Beverage.TALL:
            extra = 0.10
        elif size == Beverage.GRANDE:
            extra = 0.20
        else:  # VENTI
            extra = 0.25
        return self._beverage.cost() + extra

class Whip(CondimentDecorator):
    """
    Decorador para añadir Crema a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Crema"

    def cost(self) -> float:
        size = self.get_size()
        if size == Beverage.TALL:
            extra = 0.10
        elif size == Beverage.GRANDE:
            extra = 0.15
        else:  # VENTI
            extra = 0.20
        return self._beverage.cost() + extra

class Caramel(CondimentDecorator):
    """
    Decorador para añadir Caramel a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Caramelo"

    def cost(self) -> float:
        return self._beverage.cost() + 0.20
