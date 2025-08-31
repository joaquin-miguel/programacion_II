import pytest
from TP2_patron_decorator.decorador.beverages import Espresso
from TP2_patron_decorator.decorador.condiments import Mocha, Whip, Soy, Caramel

def test_espresso_doble_caramelo_y_whip():
    pedido1 = Espresso()
    pedido1 = Caramel(pedido1)
    pedido1 = Caramel(pedido1)
    pedido1 = Whip(pedido1)
    assert pedido1.get_description() == "Espresso, Caramelo, Caramelo, Crema"
    assert pedido1.cost() == 1.99 + 0.20 + 0.20 + 0.10

