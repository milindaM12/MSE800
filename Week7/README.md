Animals is an abstract superclass.
Dog and Cat are subclasses.
This means Dog inherits from Animals.
Cat also inherits from Animals. (code demonstrates inheritance and polymorphism.)

Issue is, DogFactory.create_product() contains: pass
So not implemented. 
So factory.create_product() returns None.
AttributeError:
'NoneType' object has no attribute 'run'