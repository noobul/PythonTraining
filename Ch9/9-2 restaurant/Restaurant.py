class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is called {self.restaurant_name}")
        print(f"The restaurant servs {self.cuisine_type}")

    def open_restaurant(self, open_mesage):
        print(open_mesage)