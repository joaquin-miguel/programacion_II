from subject_encrypter import SujetoEncriptador
from observers_encrypter import Suscriptor

def main():
    url = "https://jsonplaceholder.typicode.com/posts/1"  # API pública de prueba

    subject_push = SujetoEncriptador(modo="push")

    obs1 = Suscriptor(subject_push, nombre="Subscriptor-P1", modo="push")
    obs2 = Suscriptor(subject_push, nombre="Subscriptor-P2", modo="push")

    print("==============================================================================")
    print("=== Notificación Push desde Internet ===")
    print("==============================================================================")
    subject_push.setear_mensaje_desde_url(url)
    
    #----------------------------------------------------------#

    subject_pull = SujetoEncriptador(modo="pull")
    
    obs3 = Suscriptor(subject_pull, nombre="Subscriptor-L1", modo="pull")
    obs4 = Suscriptor(subject_pull, nombre="Subscriptor-L2", modo="pull")
    print("==============================================================================")
    print("=== Notificación Pull desde Internet ===")
    print("==============================================================================")
    subject_pull.setear_mensaje_desde_url(url)
    print("==============================================================================")

if __name__ == "__main__":
    main()


