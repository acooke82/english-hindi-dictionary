"""import abc
from model.enums import *
from model.word import Word


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_dictionary(self) -> list[Word]:
        raise NotImplementedError
