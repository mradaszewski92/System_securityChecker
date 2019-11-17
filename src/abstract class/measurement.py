from abc import ABC, abstractclassmethod, abstractmethod


class Measurement(ABC):
    @abstractmethod
    def get_execution_time(self):
        pass

    @abstractmethod
    def write_logs(self, path):
        pass
