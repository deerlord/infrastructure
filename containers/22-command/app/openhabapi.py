from openhab import OpenHAB

hab = OpenHAB('http://openhab:8080/rest')

ITEM_ACTIONS = [
    'on',
    'off',
    'increase',
    'decrease',
    'up',
    'down',
    'stop',
]

EXTERNAL_COMMANDS = [
    'play',
]


class ExternalCommands:
    def play(request):
        return True


def request(data):
    if data['command'] in EXTERNAL_COMMANDS:
        cmd = getattr(ExternalCommands, data['command'])
        args = [data['item'],]
    elif data['commmand'] in ITEM_ACTIONS:
        # get item
        if not hasattr(item, data['command']):
            return None
        cmd = getattr(item, data['command'])
        args = []
    elif isinstance(data['command']):
        if not hasattr(item, 'command'):
            return None
        cmd = getattr(item, 'command')
        args = [data['command'],]
    else:
        pass  # no command sent
    return cmd(*args)
