from beverages import Beverage
from condiments import CondimentDecorator
from typing import TypeVar, Type

BeverageType = TypeVar('BeverageType', bound='Beverage')

def build_beverage(base: BeverageType, size:str, condiments:list[Type[CondimentDecorator]]) -> Beverage:
    '''
    Funcion para armar una bebida en una linea
    Uso: build_beverage(Espresso, Beverage.TALL, [Caramel, Caramel, Whip])
    '''
    beverage = base()
    beverage.set_size(size)

    for condimento in condiments:
        beverage = condimento(beverage)

    return beverage