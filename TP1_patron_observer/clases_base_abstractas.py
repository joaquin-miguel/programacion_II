from abc import ABC, abstractmethod

class Sujeto(ABC):
    @abstractmethod
    def registrar_observador(self, observer):
        pass

    @abstractmethod
    def remover_observador(self, observer):
        pass

    @abstractmethod
    def notificar_observador(self):
        pass

class Observador(ABC):
    @abstractmethod
    def update(self, data=None): 
        """En Push recibe data; en Pull ignora y consulta al Subject"""
        pass

