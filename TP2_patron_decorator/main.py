# main.py
# Script principal para probar el patrón Decorator.

from decorador.beverages import Espresso, DarkRoast, HouseBlend, Beverage
from decorador.condiments import Mocha, Whip, Soy, Caramel
import decorador.builder as builder



def main():
    print("Bienvenido a Starbuzz Coffee!")
    print("--- Preparando pedidos ---")

    # Pedido 1: Un Espresso simple, sin condimentos.
    beverage1 = Espresso()
    print(f"Pedido 1: {beverage1.get_description()} ${beverage1.cost():.2f}")

    # Pedido 2: Un DarkRoast con doble Mocha y Crema.
    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(f"Pedido 2: {beverage2.get_description()} ${beverage2.cost():.2f}")

    # Pedido 3: Un HouseBlend con Soja, Mocha y Crema.
    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"Pedido 3: {beverage3.get_description()} ${beverage3.cost():.2f}")

    # Pedido 4: Un HouseBlend VENTI con Soja, Mocha y Crema.
    beverage4 = HouseBlend()
    beverage4.set_size(Beverage.VENTI)
    beverage4 = Soy(beverage4)
    beverage4 = Mocha(beverage4)
    beverage4 = Whip(beverage4)
    print(f"Pedido 4: {beverage4.get_description()} ${beverage4.cost():.2f}")

    # Pedido 5: Un Espresso con Caramelo y Crema
    beverage5 = Espresso()
    beverage5 = Caramel(beverage5)
    beverage5 = Whip(beverage5)
    print(f"Pedido 5: {beverage5.get_description()}  ${beverage5.cost():.2f}")

    # Pedido 6
    beverage6 = builder.build_beverage(Espresso, Beverage.TALL, [Caramel, Caramel, Whip])
    print(f"Pedido 6: {beverage6.get_description()}, ${beverage6.cost():.2f}")

    beverage7 = builder.build_beverage(Espresso, Beverage.TALL, [Whip, Mocha,  Whip, Caramel, Mocha, Whip])
    print(beverage7.get_description())
    print(f"Pedido 7: {beverage7.pretty_descripcion()}, ${beverage7.cost():.2f}")

    
if __name__ == "__main__":
    main()