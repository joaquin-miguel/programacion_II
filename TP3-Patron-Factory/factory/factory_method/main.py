from .store import NYPizzaStore, ChicagoPizzaStore

def main():
    ny = NYPizzaStore(); 
    chi = ChicagoPizzaStore()

    p1 = ny.order_pizza("cheese"); 
    print("Ethan ordered:", p1)
    print("*----------------------------------*")
    p2 = chi.order_pizza("cheese"); 
    print("Joel ordered:", p2)
    print("*----------------------------------*")
    p3 = ny.order_pizza("veggie"); 
    print("John ordered:", p3)
    print("*----------------------------------*")
    p4 = chi.order_pizza("veggie"); 
    print("George ordered:", p4)
    print("*----------------------------------*")
    p5 = ny.order_pizza("pepperoni"); 
    print("Kevin ordered:", p5)
    print("*----------------------------------*")
    p6 = chi.order_pizza("pepperoni"); 
    print("Stuart ordered:", p6)
    print("*----------------------------------*")

if __name__ == "__main__":
    main()
