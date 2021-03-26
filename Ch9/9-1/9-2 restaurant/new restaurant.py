import Restaurant 

pizza_restaurant = Restaurant.Restaurant('La pomodori', 'Pizza')
shaworma_restaurant = Restaurant.Restaurant('Mama Manu', 'Shaworma')
soup_restaurant = Restaurant.Restaurant('Souper', 'Soup')

ic_stand = Restaurant.IceCreamStand('Gelato', 'Ice Cream')

restaurants = [pizza_restaurant, shaworma_restaurant, soup_restaurant, ic_stand]

def restaurant_status():
    for restaurant in restaurants:

        print(restaurant.restaurant_name)
        print(restaurant.cuisine_type)
        print(restaurant.number_served)

        restaurant.describe_restaurant()

        message = f"The {restaurant.restaurant_name} restauranat is now open."
        restaurant.open_restaurant(message)

restaurant_status()

pizza_restaurant.set_number_served(20)
shaworma_restaurant.set_number_served(35)
soup_restaurant.set_number_served(1)

restaurant_status()

pizza_restaurant.increment_number_served(5)
shaworma_restaurant.increment_number_served(7)
soup_restaurant.increment_number_served(5)

restaurant_status()

flavors = ['vanila', 'chocolate']

ic_stand.add_flavors(flavors)
ic_stand.display_flavors()