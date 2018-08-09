from abc import ABCMeta, abstractmethod

class Procesor(object):
    __metaclass__ = ABCMeta

    def __init__(self, type):
        self.type = type

    @abstractmethod
    def process(self):
        pass

    def addValue(self, value):
        self.values.append(value)