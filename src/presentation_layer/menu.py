from presentation_layer.terminal import Terminal
from abc import abstractmethod

class Menu:
    def __init__(self, terminal: Terminal):
        self.terminal:Terminal = terminal

    @abstractmethod
    def render() -> None:
        pass