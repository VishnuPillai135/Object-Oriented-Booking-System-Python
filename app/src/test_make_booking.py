from src.client import bootstrap_system

class TestMakeBooking(object):

    def setup_method(self):
        from src.AuthenticationManager import DummyAuthenticationManager
        self.system = bootstrap_system(DummyAuthenticationManager())
        
    def test_unsuccessful_make_small_car_booking(self):
        print("test successful make small car booking")
        start_location = 'Sydeny'
        end_location = 'Melbourne'
        start_date = '2018-6-20'
        end_date = '2018-6-23'
        
        car = self.system.cars[0]
        user = self.system.login_customer('Matt', 'pass')
        
        self.system.make_booking(user, car, start_date, end_date, start_location, end_location)
        
        assert len(self.system._bookings) == 1
        assert self.system._bookings[0].booking_fee == 200
        assert self.system._bookings[0].location.pickup == start_location
        assert self.system._bookings[0].location.dropoff == end_location   
     
    def test_unsuccessful_make_medium_car_booking(self):
        print("test successful make medium car booking")
        start_location = 'China'
        end_location = 'Africa'
        start_date = '2018-12-12'
        end_date = '2018-12-24'
        
        car = self.system.cars[1]
        user = self.system.login_customer('Matt', 'pass')
        
        self.system.make_booking(user, car, start_date, end_date, start_location, end_location)
        
        assert len(self.system._bookings) == 1
        assert self.system._bookings[1].booking_fee == 650
        assert self.system._bookings[1].location.pickup == start_location
        assert self.system._bookings[1].location.dropoff == end_location   
        
    def test_unsuccessful_make_premium_car_booking(self):
        print("test successful make premium car booking")
        start_location = 'Greece'
        end_location = 'America'
        start_date = '2018-11-1'
        end_date = '2018-12-28'
        
        car = self.system.cars[35]
        user = self.system.login_customer('George', 'pass')
        
        self.system.make_booking(user, car, start_date, end_date, start_location, end_location)
        
        assert len(self.system._bookings) == 1
        assert self.system._bookings[2].booking_fee == 10005
        assert self.system._bookings[2].location.pickup == start_location
        assert self.system._bookings[2].location.dropoff == end_location           
