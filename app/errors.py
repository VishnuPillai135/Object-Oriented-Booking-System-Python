from datetime import datetime


class BookingError(Exception):

    def __init__(self, message, field):
        self._message = message
        self._field = field
        
def check_location_error(location):
    if location.pickup == "" or location.dropoff == "":
        raise BookingError("Specify a valid location",location.pickup)
    return True  

#def validate_location(location): 
#    errors = {}
#    try:
#        return check_location_error(location)
#    except BookingError as a:
#        print(a._message)
#        errors['location'] = a._message    
#    return errors   

def validate(date):
    try:
        datetime.strptime(str(date), '%Y-%m-%d')
    except ValueError:
        raise BookingError("Specify a valid date", date)
#        print("Incorrect data format, should be YYYY-MM-DD")
