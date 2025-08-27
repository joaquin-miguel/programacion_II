import base64
import requests
from clases_base_abstractas import Sujeto

class SujetoEncriptador(Sujeto):
    def __init__(self, modo="push"):
        self._observadores = []
        self._mensaje = ""
        self._modo = modo  # "push" o "pull"

    def registrar_observador(self, observador):
        if observador not in self._observadores:
            self._observadores.append(observador)

    def remover_observador(self, observador):
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar_observador(self):
        for observador in self._observadores:
            if self._modo == "push":
                observador.update(self._mensaje)   # push
            else:
                observador.update()               # pull

    def setear_mensaje(self, mensaje: str):
        encoded = base64.b64encode(mensaje.encode("utf-8")).decode("utf-8")
        self._mensaje = encoded
        self.notificar_observador()

    def setear_mensaje_desde_url(self, url: str):
        """Descarga un post de internet y lo notifica"""
        try:
            resp = requests.get(url, timeout=5)
            if resp.status_code == 200:
                # Tomamos las primeras 200 chars del contenido como ejemplo
                text = resp.text[:200]
                self.setear_mensaje(f"Post de internet: {text}")
            else:
                self.setear_mensaje(f"Error al obtener contenido de {url}")
        except Exception as e:
            self.setear_mensaje(f"Excepción al descargar: {e}")
        
    # Getter para Pull
    def obtener_mensaje(self):
        return self._mensaje
