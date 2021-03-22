def make_car(manufacturer, model, **car_details):
    """Create car details"""
    car_details["manufacturer_name"] = manufacturer.title()
    car_details["model_name"] = model.title()
    return car_details

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)