def make_car(car_brand,car_name,**car_info):
    car_info['brand'] = car_brand
    car_info['name'] = car_name
    return car_info
car = make_car('スバル','レガシィ',color='ブルー',recorder=True)

print(car)