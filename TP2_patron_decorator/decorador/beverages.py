# beverages.py
# Contiene el Componente y los Componentes Concretos del patrón.

from abc import ABC, abstractmethod

# --- Componente Abstracto ---
class Beverage(ABC):
    """
    La clase base para todas las bebidas. Utiliza el módulo abc para
    definir que es una clase abstracta.
    """
    TALL = "Tall"
    GRANDE = "Grande"
    VENTI = "Venti"

    def __init__(self, size = TALL):
        self.description = "Bebida Desconocida"
        self.size = size

    def get_description(self) -> str:
        """
        Devuelve la descripción de la bebida.
        """
        return f'{self.description} {self.get_size()}'

    def pretty_descripcion(self):
        lista_condimentos: list = self.get_description().split(', ')

        # Guardo el tipo de Bebida
        descripcion: str = lista_condimentos[0]

        lista_condimentos.remove(descripcion)

        zip_condimentos = zip(lista_condimentos,
                              map(lambda condimento:
                                  lista_condimentos.count(condimento)
                                  , lista_condimentos)
        )

        dict_condimentos = dict(zip_condimentos)

        for condimento, value in dict_condimentos.items():
            match value:
                case 1:
                    descripcion += f', {condimento}'
                case 2:
                    descripcion += f', Doble {condimento}'
                case 3:
                    descripcion += f', Triple {condimento}'
                case _:
                    print('es un monton')

        return descripcion

    def set_size(self, size: str):
        self.size = size

    def get_size(self) -> str:
        return self.size

    @abstractmethod
    def cost(self) -> float:
        """
        Método abstracto que las subclases deben implementar para devolver
        el costo de la bebida.
        """
        pass

# --- Componentes Concretos ---
class HouseBlend(Beverage):
    """
    Café de la casa, un tipo específico de bebida.
    """
    def __init__(self):
        super().__init__()
        self.description = "Café de la Casa"

    def cost(self) -> float:
        return 0.89

class DarkRoast(Beverage):
    """
    Café Dark Roast, un tipo específico de bebida.
    """
    def __init__(self):
        super().__init__()
        self.description = "Café Dark Roast"

    def cost(self) -> float:
        return 0.99

class Decaf(Beverage):
    """
    Café Descafeinado, un tipo específico de bebida.
    """
    def __init__(self):
        super().__init__()
        self.description = "Café Descafeinado"

    def cost(self) -> float:
        return 1.05

class Espresso(Beverage):
    """
    Café Espresso, un tipo específico de bebida.
    """
    def __init__(self):
        super().__init__()
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99