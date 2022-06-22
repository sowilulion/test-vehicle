from library.Pins import Pins
from library.Signals import Signals


class Library(Pins,
              Signals):
    """Пакет для получения API стендов"""
    def __init__(self):
        super(Library, self).__init__()
