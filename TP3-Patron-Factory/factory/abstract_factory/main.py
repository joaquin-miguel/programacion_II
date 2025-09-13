from factory.store import PizzaStore, NYPizzaStore, ChicagoPizzaStore

def main():
    ny = NYPizzaStore(); 

    chi = ChicagoPizzaStore()
    
    print("----------------------------------------")
    ny.order_pizza("cheese")
    print("----------------------------------------")
    chi.order_pizza("clam")
    print("----------------------------------------")

    ny.order_pizza("veggie")
    print("----------------------------------------")
    chi.order_pizza("pepperoni")
    print("----------------------------------------")
    
if __name__ == "__main__":
    main()
