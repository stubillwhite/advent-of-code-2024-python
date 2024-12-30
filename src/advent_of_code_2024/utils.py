from dataclasses import dataclass


@dataclass
class AbstractDataclass:

    def __new__(cls, *args, **kwargs):
        if cls == AbstractDataclass or cls.__bases__[0] == AbstractDataclass:
            raise TypeError("Attempted to instantiate abstract class.")
        return super().__new__(cls)
