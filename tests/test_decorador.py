import pytest
from TP2_patron_decorator.decorador.beverages import Espresso, Beverage
from TP2_patron_decorator.decorador.condiments import Whip, Mocha, Caramel
from TP2_patron_decorator.decorador.builder import build_beverage

def test_espresso_doble_caramelo_y_whip():
    pedido_1 = build_beverage(Espresso, Beverage.TALL, [Whip, Mocha,  Whip, Caramel, Mocha, Whip])
    
    assert pedido_1.get_description() == "Espresso Tall, Crema, Mocha, Crema, Caramelo, Mocha, Crema"
    assert pedido_1.pretty_descripcion() == 'Espresso Tall, Triple Crema, Doble Mocha, Caramelo'
    assert pedido_1.cost() == 1.99 + 0.1 + 0.1 + 0.1 + 0.2 + 0.2 + 0.2
    


