import base64
from clases_base_abstractas import Observador

class Suscriptor(Observador):
    def __init__(self, sujeto, nombre="Observador", modo="push"):
        self._sujeto = sujeto
        self._nombre = nombre
        self._modo = modo
        sujeto.registrar_observador(self)

    def update(self, data=None):
        if self._modo == "push":
            decoded = base64.b64decode(data).decode("utf-8")
        else:  # pull
            encoded = self._sujeto.obtener_mensaje()
            decoded = base64.b64decode(encoded).decode("utf-8")

        print(f"[{self._nombre}] recibió actualización: {decoded}")
        print("--------------------------------------------------------------------------")
