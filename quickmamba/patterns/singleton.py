class Singleton(object):
    def __new__(type):
        if '_the_instance' not in type.__dict__:
            type._the_instance = object.__new__(type)
        return type._the_instance


