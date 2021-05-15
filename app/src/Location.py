class Centre:
    def __init__(self,name,suburb,providers,rating):
        self._name  = name
        self._suburb = suburb
        self._rating = rating
        self._providers = providers #should be a list of providers in the centre

    @property
    def name(self):
        return self._name
    
    @property    
    def rating(self):
        return self._rating 
        
    @rating.setter
    def rating(self, rating):
        self._rating = rating
             
    @property
    def suburb(self):
        return self._suburb  
        
    @property
    def providers(self):
        return self._providers        
    
    def add_provider(self, provider):
        providers.append(provider)
        pass
        
    def __str__(self):
        return f'Centre: {self.name}'
