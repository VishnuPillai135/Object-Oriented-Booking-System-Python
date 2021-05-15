from src.Booking import Booking
import copy
from errors import *
from flask_login import login_required, current_user

class BookingSystem:
    def __init__(self, admin_system, auth_manager):
        self._providers = []
        self._locations = []
        self._patients = []
        self._bookings = []
        self._admin_system = admin_system
        self._auth_manager = auth_manager


    '''
    Query Processing Services
    '''
    def provider_search(self,name=None):
        search = []
          
        for provider in self._providers:
            if name in provider.name: #is the keyword in the search
                print(provider.name)
                search.append(provider)           
        return search
        
    def location_search(self,name=None):
        search = []
        for location in self._locations:
            print(location.name)
            if name in location.name: #is the keyword in the search
                search.append(location)             
        return search    
        
    def suburb_search(self,suburb=None):
        search = []
        for location in self._locations:
            if suburb in location.suburb: #is the keyword in the search
                search.append(location)             
        return search   
         
    def type_search(self,service=None):
        search = []
        if provider in self._providers:
            if provider.service == service: #is the keyword in the search
                search.append(provider)           
        return search      
    #add search by location above
    
    
    
    def get_user_by_id(self, user_id):
        for c in self._patients:
            if c.get_id() == user_id:
                return c

        return self._admin_system.get_user_by_id(user_id)
            

    def get_provider(self, provnum):
        for c in self.providers:
            if c.provnum == provnum:
                print(c)
                return c
        return None
        
    def get_location(self, location):
        for c in self.locations:
            if c.name == location:
                return c
        return None    
    
    '''
    Booking Services
    '''
    def make_booking(self, patient,time,date, provider,reason):
        # Prevent the patient from referencing 'current_user';
        # otherwise the patient recorded in each booking will be modified to
        # a different user whenever the current_user changes (i.e. when new user logs-in)
        patient = copy.copy(patient)
        
        #check_location_error(location)
        #validate(start_date)
        new_booking = Booking(patient,time,date, provider,reason)
        
        self._bookings.append(new_booking)
        provider.add_booking(new_booking)
        current_user.add_booking(new_booking)
        
        return new_booking
    


    '''
    Registration Services
    '''
    def add_provider(self, Provider):
        self._providers.append(Provider)


    def add_patient(self, Patient):
        self._patients.append(Patient)
        
    def add_location(self, Centre):
        self._locations.append(Centre)     



    '''
    Login Services
    '''

    def login_patient(self, username, password):
        for patient in self._patients:
            if self._auth_manager.login(patient, username, password):
                return True
        return False

    def login_admin(self, username, password):
        return self._admin_system.login(username, password)
        

    '''
    Properties
    '''
    @property
    def providers(self):
        return self._providers
        
    @property
    def locations(self):
        return self._locations


    @property
    def bookings(self):
        return self._bookings
