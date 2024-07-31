import abc
from model.enums import *
from model.word import Word
from typing import List


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_dictionary(self) -> List[Word]:
        raise NotImplementedError
