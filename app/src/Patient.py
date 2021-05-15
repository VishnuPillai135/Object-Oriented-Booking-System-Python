from flask_login import UserMixin
from abc import ABC, abstractmethod


class User(UserMixin, ABC):
    __id = -1

    def __init__(self, username, password,email,name,phone):
        self._id = self._generate_id()
        self._username = username
        self._password = password
        self._email = email
        self._name = name
        self._phone = phone
        self._bookings = []

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
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password
        
    @property
    def bookings(self):
        return self._bookings    
            
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        """Required by Flask-login"""
        return str(self._id)

    def _generate_id(self):
        User.__id += 1
        return User.__id

    def validate_password(self, password):
        return self._password == password
    
    def add_booking(self, booking):
        self.bookings.append(booking) 
        

    @abstractmethod
    def is_admin(self):
        pass
    
    @username.setter
    def username(self, username):
        self._username = username  
        
    @email.setter
    def email(self, email):
        self._email = email    
    
    @phone.setter
    def phone(self, number):
        self._phone = number
        
    @password.setter
    def password(self, password):
        self._password = password             
    

class Patient(User):

    def __init__(self, username, password,email,name,phone,medicare):
        super().__init__(username, password,email,name,phone)
        self._medicare = medicare
  
    @property
    def medicare(self):
        return self._medicare 
    
    def is_admin(self):
        return False

    def __str__(self):
        return f'Patient Name: {self._username}, Medicare: {self._medicare}'


class Admin(User):
    
    def __init__(self, username, password,email,name,phone):
        super().__init__(username, password,email,name,phone)   

    def is_admin(self):
        return True

    def __str__(self):
        return f'Provider name: {self._username}'
