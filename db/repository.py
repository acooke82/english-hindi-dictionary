import abc
from model.enums import *
from model.givenentry import GivenEntry


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_dictionary(self) -> list[GivenEntry]:
        raise NotImplementedError