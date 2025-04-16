from abc import ABC # , abstractmethod
class User(ABC):
    def __init__(self,name,email,nid)->None: # ->None is used to specify the return type of the function
        self.name=name
        