
import random

class Bird:
    def __init__(self, name):
        self._name = name
    def get_name(self):
        return self._name
    def can_fly(self):
        return True
    def colour(self):
        return('multi-coloured')
    def can_be_feeded(self):
        return False
    def you_can_touch(self):
        return False
    
class WildBird(Bird): #Полиморфизм
    def __init__(self, name):
        super().__init__(name)
        

class HomeBird(Bird): #Полиморфизм
    def __init__(self, name):
        super().__init__(name)
        
    def can_be_feeded(self):
        return True
    
    
class Calibri(WildBird): #Полиморфизм  
    def __init__(self, name):
        super().__init__(name)
    
    def colour(self):
        return 'Blue'

class Chicken(HomeBird): #Полиморфизм  
    def __init__(self, name):
        super().__init__(name)
    
    def colour(self):
        return 'White'
    
    def you_can_touch(self):
        if random.random() > 0.35:
            return True
        else:
            return False
            

class Owl(WildBird):   #Полиморфизм 
    def __init__(self, name):
        super().__init__(name)
    
    def colour(self):
        return 'Snowy'
        
    def you_can_touch(self):
        if random.random() > 0.75:
            return True
        else:
            return False

class Goose(HomeBird):   #Полиморфизм
    def __init__(self, name):
        super().__init__(name)

    def colour(self):
        return 'White'
        
    def you_can_touch(self):
        if random.random() > 0.85:
            return True
        else:
            return False

class Human:
    def __init__(self, birdy):
        self.birdy = birdy
        
    def hooman_and_birdy(self):
        if self.birdy.you_can_touch() == True and self.birdy.can_be_feeded() == True:
            return 'Hooman can feed and touch %s %s' % (self.birdy.colour(), self.birdy.get_name())
        else:
            return "%s %s is a wild bird" % (self.birdy.colour(), self.birdy.get_name())
        
birdybird = Chicken('Liza')
human = Human(birdybird)
print(human.hooman_and_birdy())
birdybird2 = Owl('Hedwig')
human2 = Human(birdybird2)
print(human2.hooman_and_birdy())
