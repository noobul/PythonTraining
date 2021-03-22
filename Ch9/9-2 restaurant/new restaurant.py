import Restaurant 

new_restaurant = Restaurant.Restaurant('La pomodori', 'Pizza')
print(new_restaurant.restaurant_name)
print(new_restaurant.cuisine_type)

new_restaurant.describe_restaurant()

message = "The restauranat is now open."
new_restaurant.open_restaurant(message)