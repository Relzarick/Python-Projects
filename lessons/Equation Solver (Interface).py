from abc import ABC, abstractmethod

class Equation(ABC):
    degree: int
    
    def __init__(self, *args):
        if (self.degree + 1) != len(args):
            raise TypeError(
                f"'Equation' object takes {self.degree + 1} positional arguments but {len(args)} were given"
            )
        if any(not isinstance(arg, (int, float)) for arg in args):
            raise TypeError("Coefficients must be of type 'int' or 'float'")
        if args[0] == 0:
            raise ValueError("Highest degree coefficient must be different from zero")
        
    def __init_subclass__(cls):
        if not hasattr(cls, "degree"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'degree'"
            )
    
    @abstractmethod
    def solve(self):
        pass
        
    @abstractmethod
    def analyze(self):
        pass
        
class LinearEquation(Equation):
    degree = 1
    
    def solve(self):
        pass
    
    def analyze(self):
        pass

    
lin_eq = LinearEquation(2, 3)




# * Any class that uses the interface MUST have an implementation of the method
# * With the same signature i.e. name, parem and return type(if applicable)
# * Actual implementation can be anything I want.
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *