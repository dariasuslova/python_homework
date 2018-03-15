class UniqObject:
    obj = None
    
    def __init__(self, name):
        self.name = name
        
    @classmethod
    def create_object(cls):
        if cls.obj is None:
            cls.obj = UniqObject('object')
        return cls.obj
    
Singleton = UniqObject('object')
print(Singleton.create_object())