from flask_login import UserMixin
import csv

class Provider:
    def __init__(self, name, email, service, phone, provnum, timeslots,rating):
        self._name = name
        self._email = email
        self._service = service
        self._phone = phone
        self._provnum = provnum
        self._bookings = []
        self._centres = []
        self._rating = rating
        self._timeslots = timeslots

    @property
    def email(self):
        return self._email
        
    @property
    def name(self):
        return self._name

    @property
    def phone(self):
        return self._phone

    @property
    def provnum(self):
        return self._provnum
        
    @property
    def centres(self):
        return self._centres   
        
    @property
    def service(self):
        return self._service   
        
    @property
    def bookings(self):
        return self._bookings
        
    @property
    def timeslots(self):
        return self._timeslots
        
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        self._rating = rating                      
       
    def add_booking(self, booking):
        self.bookings.append(booking) 
           
    def add_centres(self, centre):
        for i in centre:
            self.centres.append(i)
        
    def __str__(self):
        return f'Provider - {self.name}, {self.service}'    





