def make_car(manufacturer, model, **car_info):
    """Create a dictionary describing a car."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

build_features = make_car('ferrari', 'daytona SP3', 
                          color='red', tow_package=True)

print(build_features)
  


