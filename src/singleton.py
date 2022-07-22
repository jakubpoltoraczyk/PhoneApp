class Singleton(type):
    """Singleton class which makes possible to create only one instance of the class, used as meta class.

    Params:
        instances (dict): class parameter which contains every singleton class name as key and its instance as value"""
    instances = {}

    def __call__(cls, *args, **kwargs):
        """Method which invokes __new__ and __init__ dunder methods of base class.

        Returns:
            the first created instance of class"""
        if cls not in Singleton.instances:
            instance = type.__call__(cls, *args, **kwargs)
            Singleton.instances[cls] = instance
        return Singleton.instances[cls]
