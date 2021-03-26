class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant is called {self.restaurant_name}")
        print(f"The restaurant servs {self.cuisine_type}")

    def open_restaurant(self, open_mesage):
        print(open_mesage)

    def set_number_served(self, served):
        if served >= self.number_served:
            self.number_served = served
        else:
            print("You can't decrease the number served.")

    def increment_number_served(self, served):
        if served >= 0:
            self.number_served += served
        else:
            print("You can't decrease the number served.")

#9-6 Ice Cream Stand
class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):

        super().__init__(restaurant_name, cuisine_type)
        self.ice_cream_flavors = []

    def add_flavors(self, flavors):
        self.ice_cream_flavors = flavors

    def display_flavors(self):
        print(f"{self.ice_cream_flavors}")