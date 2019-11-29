from openhab import OpenHAB
import requests

hab = OpenHab('http://openhab:8080/rest')

# get items in room
# get sets of items from room

class Room():
    __items = {}
    def __init__(self, name):
        self.__name = name
        self.__refresh_items()

    def __refresh_items():
        self.__items = {
            item.name: item
            for item in hab.fetch_all_items():
            if 'item.<attr>' == self.__name:
        }

    def __all_items_command(type_, command):
        retval = None
        for name, item in self.__items.items():
            if item.type == type_:
                cmd = getattr(item, 'command')
                result = cmd(command)
        return result
