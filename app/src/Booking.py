class Booking(object):

    def __init__(self, patient, time,date, provider,reason):
        self._patient  = patient
        self._time = time
        self._date = date
        self._provider = provider
        self._reason  = reason #should be a string that contains the reason for visit

    @property
    def patient(self):
        return self._patient
    
    @property
    def time(self):
        return self._time  
        
    @property
    def date(self):
        return self._date
    
    @property
    def provider(self):
        return self._provider
        
    @property
    def reason(self):
        return self._reason      
          
            

    def __str__(self):
        return f'Booking for: {self._patient}'
