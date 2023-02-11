from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self):
        self._cat = None

    def set_cat(self, cat):
        self._cat = cat

    @abstractmethod
    def feed_cat(self):
        pass

    @abstractmethod
    def play_with_the_cat(self):
        pass

    @abstractmethod
    def put_the_cat_to_sleep(self):
        pass
