''' generator_base.py

    This module contains an abstract class for all of the generators
'''
from abc import ABC, abstractmethod
from utils.utils_yaml import load_yaml


class BaseGenerator(ABC):
    @abstractmethod
    def generate(self):
        raise NotImplementedError

    def load_db(self, dictionary_name):
        return load_yaml(dictionary_name)
