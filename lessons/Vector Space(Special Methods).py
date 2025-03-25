class R2Vector:
    def __init__(self, *, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return sum(val**2 for val in vars(self).values())**0.5

    def __str__(self):
        return str(tuple(getattr(self, i) for i in vars(self)))

    def __repr__(self):
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'


    def __getattr__(self, attr):                
        return 'calling __getattr__'

class R3Vector(R2Vector):
    def __init__(self, *, x, y, z):
        super().__init__(x=x, y=y)
        self.z = z

v1 = R2Vector(x=2, y=3)
v2 = R3Vector(x=2, y=2, z=3)
# print(f'v1 = {v1}', f'\nrepr = {repr(v1)}')
# print(f'v2 = {v2}', f'\nrepr = {repr(v2)}')
print(v1.z)
print(getattr(v1, 'z'))

# * __str__ returns human readable strings

# * __class__ for debuging and dynamic behavious
#   user isinstance() or issubclass() for type checks / validations

# * __getattribute__ will raise an error (overide default behaviour?)
#   called implicitly for all attributes
#   user super()

# * __getattr__ if attribute is not found, return custom logic
#   called implicitly when attribute is missing for missing attributes only

# * getattr() used for looking up able to return a default value
#   called explicitly for existing or missing attributes(allows default value)

# * __add__

# * __sub__