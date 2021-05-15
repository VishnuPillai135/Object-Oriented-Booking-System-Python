

'''
    CarFactory instantiates new Car objects from given set of
    arguments that describe what the new car should be like
'''
class CarFactory():

    def __init__(self):
        
        # define a mapping from string to class
        self._type_string_to_class = {
            'small': SmallCar, 
            'medium': MediumCar, 
            'large': LargeCar, 
            'premium': PremiumCar
            }

    def make_provider(self, name, service, rego, car_type):
        provider_type = self._type_string_to_class.get(car_type)
        if not car_class:
            return None
        
        return car_class(name, service, rego)
